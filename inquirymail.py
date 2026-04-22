import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_contact_inquiry(user_name, user_email, subject, message_body):
    # Fetch system secrets from .env
    SENDER_EMAIL = os.getenv("EMAIL_USER")
    SENDER_PASS = os.getenv("EMAIL_PASS")
    
    # Recipient Config
    HR_EMAIL = "hr@newagepetroconchem.in"
    BCC_RECIPIENTS = ["chirag.bhojak@newagepetroconchem.in","info@newagepetroconchem.in","ashok@newagepetroconchem.in"]

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASS)

            # --- 1. INTERNAL NOTIFICATION (TO HR & BCC OTHERS) ---
            internal_msg = EmailMessage()
            internal_msg["Subject"] = f"New Website Inquiry: {subject}"
            internal_msg["From"] = SENDER_EMAIL
            internal_msg["To"] = HR_EMAIL
            internal_msg["Bcc"] = ", ".join(BCC_RECIPIENTS) # Joins the list with commas

            internal_msg.set_content(f"""
New message from NPCPL Contact Us Form:

Sender: {user_name} ({user_email})
Subject: {subject}

Message Content:
{message_body}
""")
            smtp.send_message(internal_msg)

            # --- 2. AUTO-REPLY (TO CUSTOMER) ---
            auto_reply = EmailMessage()
            auto_reply["Subject"] = "Thank you for contacting NPCPL"
            auto_reply["From"] = f"New Age Petro Conchem <{SENDER_EMAIL}>"
            auto_reply["To"] = user_email 

            auto_reply.set_content(f"""
Dear {user_name},

Thank you for reaching out to New Age Petro Conchem Pvt. Ltd. (NPCPL).

We have received your inquiry regarding "{subject}" and our team is currently reviewing your message. One of our representatives will get back to you shortly.

If you have urgent requirements, please feel free to call us at +91 9825574000.

Best Regards,
Team NPCPL
Vadodara, Gujarat
www.newagepetroconchem.in
""")
            smtp.send_message(auto_reply)

        # This string is what will show up in the gold box on your website
        return "Thank you! We will contact you soon."

    except Exception as e:
        print(f"Error handling contact form: {e}")
        return "System busy. Please try again later or call us directly."