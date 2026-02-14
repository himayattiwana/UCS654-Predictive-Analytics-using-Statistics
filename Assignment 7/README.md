# Assignment 7 - Mashup (102313049)

## Submitted Files
- `102313049.py` - Program 1 (command line mashup)
- `102313049_program2.py` - Program 2 (web service mashup)
- `templates/program2.html` - Program 2 form UI
- `requirements.txt` - dependencies

## Program 1
- Implemented as required in one Python file: `102313049.py`

## Program 2 Web App Link
- [https://ucs654-predictive-analytics-using.onrender.com/](https://ucs654-predictive-analytics-using.onrender.com/)

## Issue Faced on Hosted Deployment
- On Render, YouTube blocks many `yt-dlp` requests with bot-verification/sign-in challenge.
- Because of this, some requests fail at download stage and the app can show:
  - `No files were downloaded from YouTube for this singer.`
- This is due to YouTube anti-bot restrictions on cloud/server IPs, not due to SMTP or form validation logic.

## Security Handling
- SMTP credentials are not stored in code or committed files.
- Secrets are provided via environment variables only.
