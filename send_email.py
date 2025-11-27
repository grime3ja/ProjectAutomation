import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
load_dotenv()

import os
import sys

sender_email = "jgrimes112003@gmail.com"

receiving_emails = ["jgrimes112003@gmail.com"]
receiving_emails_bcc = ["ashlyc0617@gmail.com", "jagprg@gmail.com", "jagredskin@yahoo.com", "megan92006@icloud.com"]
def prepare_email(subject, body):
  msg = EmailMessage()

  msg.set_content(body)
  msg['Subject'] = subject
  msg['From'] = sender_email
  msg['To'] = receiving_emails
  msg['Bcc'] = receiving_emails_bcc

  return msg

def send_email(msg=""):
  sender_password = os.getenv("EMAIL_PASS")

  smtp_server = "smtp.gmail.com"
  smtp_port = 587
  try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
  
    server.login(sender_email, sender_password)
  
    server.send_message(msg)
    server.quit()
  
    print("Email send successfully")
  except Exception as e:
    print("Can't send email because of", e)
    raise e

if __name__ == "__main__":
  msg = prepare_email(sys.argv[1], " ".join(sys.argv[2:]))
  send_email(msg)
