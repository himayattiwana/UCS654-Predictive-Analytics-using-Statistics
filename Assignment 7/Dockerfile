FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && rm -rf /var/lib/apt/lists/*

COPY Assignment\ 7/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY Assignment\ 7 /app

ENV PORT=10000

CMD ["sh", "-c", "gunicorn app_entry:app --bind 0.0.0.0:${PORT} --workers 2 --threads 2 --timeout 600"]
