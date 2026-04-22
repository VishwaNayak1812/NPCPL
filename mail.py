import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# This loads the variables from your .env file
load_dotenv()

def send_email_to_hr(name, candidate_email, phone, position, resume_path):
    # Fetching secrets safely
    APP_EMAIL = os.getenv("EMAIL_USER")
    APP_PASSWORD = os.getenv("EMAIL_PASS")
    HR_EMAIL = ["hr@newagepetroconchem.in","newageoil.industries@gmail.com"]

    msg = EmailMessage()
    msg["Subject"] = f"New Career Application - {name}"
    msg["From"] = APP_EMAIL
    msg["To"] = HR_EMAIL

    msg.set_content(f"""
New Candidate Application

Name: {name}
Candidate Email: {candidate_email}
Phone: {phone}
Position: {position}
""")

    # Using os.path.basename for better compatibility with Windows/Linux
    file_name = os.path.basename(resume_path)

    try:
        with open(resume_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=file_name
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(APP_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Error: {e}")
