#!/usr/bin/env python3
"""
Program 2: Web service for Mashup assignment.

Run:
  python 102313049_program2.py

Then open:
  http://127.0.0.1:5000

Required environment variables for email sending:
  SMTP_HOST
  SMTP_PORT
  SMTP_USER
  SMTP_PASS
"""

from __future__ import annotations

from collections import defaultdict, deque
import re
import shutil
import smtplib
import threading
import time
import uuid
from datetime import datetime
from email.message import EmailMessage
import os
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from flask import Flask, render_template, request
from pydub import AudioSegment
from yt_dlp import YoutubeDL


ROLL_NO = "102313049"
BASE_DIR = Path(__file__).resolve().parent
JOBS_DIR = BASE_DIR / "jobs"
ENV_FILE = BASE_DIR / ".env"

app = Flask(__name__)

REQUEST_LOGS: dict[str, deque[float]] = defaultdict(deque)
REQUEST_LOCK = threading.Lock()
RATE_LIMIT_WINDOW_SECONDS = 600
RATE_LIMIT_MAX_REQUESTS = 5


def load_local_env() -> None:
    if not ENV_FILE.exists():
        return

    for raw_line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key and key not in os.environ:
            os.environ[key] = value


load_local_env()


def validate_email(email: str) -> bool:
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, email))


def ensure_environment() -> None:
    if shutil.which("ffmpeg") is None:
        raise EnvironmentError("ffmpeg is not installed or not available in PATH.")


def prepare_job_dirs() -> tuple[str, Path, Path]:
    job_id = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:8]}"
    job_root = JOBS_DIR / job_id
    downloads_dir = job_root / "downloads"
    clips_dir = job_root / "clips"
    downloads_dir.mkdir(parents=True, exist_ok=True)
    clips_dir.mkdir(parents=True, exist_ok=True)
    return job_id, downloads_dir, clips_dir


def download_audio_files(singer_name: str, number_of_videos: int, downloads_dir: Path) -> list[Path]:
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

    audio_files = sorted(
        p
        for p in downloads_dir.iterdir()
        if p.is_file()
        and p.suffix.lower() in {".m4a", ".webm", ".opus", ".mp3", ".ogg", ".wav"}
    )

    if not audio_files:
        raise RuntimeError("No files were downloaded from YouTube for this singer.")

    return audio_files


def build_mashup(audio_files: list[Path], clip_seconds: int, clips_dir: Path, output_file: Path) -> None:
    merged_audio = AudioSegment.empty()
    clip_ms = clip_seconds * 1000

    for index, audio_file in enumerate(audio_files, start=1):
        try:
            segment = AudioSegment.from_file(audio_file)
            clip = segment[:clip_ms]
            clip.export(clips_dir / f"clip_{index:03d}.mp3", format="mp3")
            merged_audio += clip
        except Exception:
            continue

    if len(merged_audio) == 0:
        raise RuntimeError("Unable to create clips from downloaded files.")

    merged_audio.export(output_file, format="mp3")


def zip_output_file(output_file: Path) -> Path:
    zip_path = output_file.with_suffix(".zip")
    with ZipFile(zip_path, "w", ZIP_DEFLATED) as zip_file:
        zip_file.write(output_file, arcname=output_file.name)
    return zip_path


def send_email_with_attachment(recipient: str, zip_file: Path) -> None:
    smtp_host = os.environ.get("SMTP_HOST")
    smtp_port = os.environ.get("SMTP_PORT")
    smtp_user = os.environ.get("SMTP_USER")
    smtp_pass = os.environ.get("SMTP_PASS")

    if not all([smtp_host, smtp_port, smtp_user, smtp_pass]):
        raise EnvironmentError(
            "SMTP credentials are not set. Please set SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS."
        )

    message = EmailMessage()
    message["Subject"] = "Mashup Result - Program 2"
    message["From"] = smtp_user
    message["To"] = recipient
    message.set_content("Your mashup zip file is attached.")

    with open(zip_file, "rb") as file:
        message.add_attachment(
            file.read(),
            maintype="application",
            subtype="zip",
            filename=zip_file.name,
        )

    with smtplib.SMTP(smtp_host, int(smtp_port), timeout=60) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(message)


def get_client_ip() -> str:
    forwarded_for = request.headers.get("X-Forwarded-For", "")
    if forwarded_for:
        return forwarded_for.split(",")[0].strip()
    return (request.remote_addr or "unknown").strip()


def enforce_rate_limit(client_ip: str) -> None:
    now = time.time()
    with REQUEST_LOCK:
        bucket = REQUEST_LOGS[client_ip]
        while bucket and now - bucket[0] > RATE_LIMIT_WINDOW_SECONDS:
            bucket.popleft()
        if len(bucket) >= RATE_LIMIT_MAX_REQUESTS:
            raise ValueError(
                f"Rate limit exceeded. Try again after {RATE_LIMIT_WINDOW_SECONDS // 60} minutes."
            )
        bucket.append(now)


def enforce_access_key(provided_key: str) -> None:
    required_key = os.environ.get("APP_ACCESS_KEY", "").strip()
    if required_key and provided_key.strip() != required_key:
        raise ValueError("Invalid access key.")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("program2.html")

    client_ip = get_client_ip()
    access_key = request.form.get("access_key", "")
    singer_name = request.form.get("singer_name", "").strip()
    videos_raw = request.form.get("number_of_videos", "").strip()
    duration_raw = request.form.get("duration_seconds", "").strip()
    email = request.form.get("email", "").strip()

    try:
        enforce_rate_limit(client_ip)
        enforce_access_key(access_key)

        if not singer_name:
            raise ValueError("Singer name is required.")

        if not videos_raw.isdigit():
            raise ValueError("Number of videos must be a valid integer.")
        if not duration_raw.isdigit():
            raise ValueError("Duration must be a valid integer.")

        number_of_videos = int(videos_raw)
        duration_seconds = int(duration_raw)

        if number_of_videos <= 10:
            raise ValueError("Number of videos must be greater than 10.")
        if duration_seconds <= 20:
            raise ValueError("Duration must be greater than 20 seconds.")
        if not validate_email(email):
            raise ValueError("Email id is invalid.")

        ensure_environment()
        job_id, downloads_dir, clips_dir = prepare_job_dirs()
        output_file = JOBS_DIR / job_id / f"{ROLL_NO}-output.mp3"

        audio_files = download_audio_files(singer_name, number_of_videos, downloads_dir)
        build_mashup(audio_files, duration_seconds, clips_dir, output_file)
        zip_file = zip_output_file(output_file)
        send_email_with_attachment(email, zip_file)

        return render_template(
            "program2.html",
            success=f"Success. Mashup created and emailed to {email}.",
            singer_name=singer_name,
            number_of_videos=number_of_videos,
            duration_seconds=duration_seconds,
            email=email,
        )

    except Exception as exc:
        return render_template(
            "program2.html",
            error=str(exc),
            singer_name=singer_name,
            number_of_videos=videos_raw,
            duration_seconds=duration_raw,
            email=email,
        )


if __name__ == "__main__":
    RATE_LIMIT_WINDOW_SECONDS = int(os.environ.get("RATE_LIMIT_WINDOW_SECONDS", "600"))
    RATE_LIMIT_MAX_REQUESTS = int(os.environ.get("RATE_LIMIT_MAX_REQUESTS", "5"))
    JOBS_DIR.mkdir(parents=True, exist_ok=True)
    app.run(
        host=os.environ.get("HOST", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("FLASK_DEBUG", "false").lower() == "true",
    )
