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

```bash
python 102313049_program2.py
```
Then open `http://127.0.0.1:5000`.
