from flask import Flask, render_template, request
from topsis_logic import run_topsis
import os
import re
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

EMAIL_REGEX = r"^[^@]+@[^@]+\.[^@]+$"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        sender_email = request.form["sender_email"]
        sender_password = request.form["sender_password"]
        receiver_email = request.form["receiver_email"]

        if not re.match(EMAIL_REGEX, sender_email) or not re.match(EMAIL_REGEX, receiver_email):
            return "Invalid email format"

        if not file:
            return "No file uploaded"

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(RESULT_FOLDER, "result.csv")

        file.save(input_path)

        result = run_topsis(input_path, weights, impacts, output_path)

        if result != "success":
            return result

        send_email(sender_email, sender_password, receiver_email, output_path)

        return "Result sent to your email"

    return render_template("index.html")

def send_email(sender, password, receiver, attachment_path):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Attached is your TOPSIS result file")

    with open(attachment_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="csv", filename="result.csv")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True)
