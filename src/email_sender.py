# src/email_sender.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from . import config

def send_email(subject: str, to_email: str, attachment_path: str):
    try:
        # Set up the email
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = config.EMAIL_USER
        msg['To'] = to_email

        # Attach the report
        with open(attachment_path, 'rb') as f:
            part = MIMEApplication(f.read(), Name='report.pdf')
            msg.attach(part)

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(config.EMAIL_USER, config.EMAIL_PASSWORD)
            server.send_message(msg)
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")