# Assignment 7 - Mashup

## Files
- `102313049.py` - Program 1 (command line mashup)
- `102313049_program2.py` - Program 2 (web service mashup)
- `templates/program2.html` - HTML form for Program 2
- `requirements.txt` - Python dependencies

## Setup
```bash
python3.11 -m venv mashup311
source mashup311/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Program 1
```bash
python 102313049.py "Bruno Mars" 20 30 102313049-bruno-output.mp3
```

## Program 2
Set SMTP env vars before running:
- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USER`
- `SMTP_PASS`
- `APP_ACCESS_KEY` (recommended for public deployment)

```bash
python 102313049_program2.py
```
Then open `http://127.0.0.1:5000`.

## Security Notes
- Do not commit `.env` to GitHub.
- Put real SMTP values in deployment platform secrets (Render/Railway/etc), not in code.
- Use Gmail App Password, not your Gmail login password.

## Render Deployment
1. Push this folder to GitHub (already done in your repo).
2. In Render, create a new **Blueprint** and select this repository.
3. Render will detect `render.yaml` and create the web service.
4. In service Environment variables, set:
   - `APP_ACCESS_KEY`
   - `SMTP_HOST`
   - `SMTP_PORT`
   - `SMTP_USER`
   - `SMTP_PASS`
5. Deploy and open the generated Render URL.
