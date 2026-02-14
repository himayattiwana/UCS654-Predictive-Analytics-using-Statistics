#!/usr/bin/env python3
"""
Program 1: Command-line Mashup generator.

Usage:
  python 102313049.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>

Example:
  python 102313049.py "Sharry Maan" 20 20 102313049-output.mp3

Dependencies (PyPI):
  pip install yt-dlp pydub

System dependency:
  ffmpeg must be installed and available in PATH.
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path
from typing import List

from pydub import AudioSegment
from yt_dlp import YoutubeDL


def print_usage() -> None:
    print(
        "Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>"
    )
    print('Example: python 102313049.py "Sharry Maan" 20 20 102313049-output.mp3')


def validate_inputs(args: List[str]) -> tuple[str, int, int, str]:
    if len(args) != 4:
        raise ValueError("Incorrect number of parameters.")

    singer_name = args[0].strip()
    if not singer_name:
        raise ValueError("Singer name must not be empty.")

    try:
        number_of_videos = int(args[1])
    except ValueError as exc:
        raise ValueError("NumberOfVideos must be an integer.") from exc

    try:
        clip_duration_seconds = int(args[2])
    except ValueError as exc:
        raise ValueError("AudioDuration must be an integer.") from exc

    if number_of_videos <= 10:
        raise ValueError("NumberOfVideos must be greater than 10.")

    if clip_duration_seconds <= 20:
        raise ValueError("AudioDuration must be greater than 20 seconds.")

    output_file_name = args[3].strip()
    if not output_file_name:
        raise ValueError("OutputFileName must not be empty.")

    return singer_name, number_of_videos, clip_duration_seconds, output_file_name


def ensure_environment() -> None:
    if shutil.which("ffmpeg") is None:
        raise EnvironmentError(
            "ffmpeg is not installed or not in PATH. Install ffmpeg to continue."
        )


def prepare_dirs(base_dir: Path) -> tuple[Path, Path]:
    downloads_dir = base_dir / "downloads"
    clips_dir = base_dir / "clips"

    for directory in (downloads_dir, clips_dir):
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True, exist_ok=True)

    return downloads_dir, clips_dir


def download_videos(singer_name: str, number_of_videos: int, downloads_dir: Path) -> List[Path]:
    search_query = f"ytsearch{number_of_videos}:{singer_name} songs"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(downloads_dir / "%(title).120s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "restrictfilenames": True,
        "ignoreerrors": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

    video_files = sorted(
        [
            p
            for p in downloads_dir.iterdir()
            if p.is_file()
            and p.suffix.lower() in {".m4a", ".webm", ".opus", ".mp3", ".ogg", ".wav"}
        ]
    )

    if not video_files:
        raise RuntimeError("No videos were downloaded. Try another singer name.")

    return video_files


def build_mashup(
    video_files: List[Path], clip_duration_seconds: int, clips_dir: Path, output_file_path: Path
) -> None:
    merged_audio = AudioSegment.empty()
    clip_duration_ms = clip_duration_seconds * 1000

    for index, video_file in enumerate(video_files, start=1):
        try:
            audio = AudioSegment.from_file(video_file)
            clip = audio[:clip_duration_ms]
            clip_path = clips_dir / f"clip_{index:03d}.mp3"
            clip.export(clip_path, format="mp3")
            merged_audio += clip
        except Exception as exc:
            print(f"Skipping file due to processing error: {video_file.name} ({exc})")

    if len(merged_audio) == 0:
        raise RuntimeError("No audio clips could be created from downloaded videos.")

    output_format = output_file_path.suffix.lstrip(".").lower() or "mp3"
    if not output_file_path.suffix:
        output_file_path = output_file_path.with_suffix(".mp3")
        output_format = "mp3"

    merged_audio.export(output_file_path, format=output_format)
    print(f"Mashup created successfully: {output_file_path}")


def main() -> int:
    try:
        singer_name, number_of_videos, clip_duration_seconds, output_file_name = validate_inputs(
            sys.argv[1:]
        )
        ensure_environment()

        base_dir = Path.cwd()
        downloads_dir, clips_dir = prepare_dirs(base_dir)
        output_file_path = base_dir / output_file_name

        print(f"Downloading {number_of_videos} videos for singer: {singer_name}")
        video_files = download_videos(singer_name, number_of_videos, downloads_dir)
        print(f"Downloaded {len(video_files)} files. Building mashup...")

        build_mashup(video_files, clip_duration_seconds, clips_dir, output_file_path)
        return 0

    except ValueError as exc:
        print(f"Input Error: {exc}")
        print_usage()
        return 1
    except EnvironmentError as exc:
        print(f"Environment Error: {exc}")
        return 1
    except Exception as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
