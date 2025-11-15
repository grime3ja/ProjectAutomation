import smtplib

from dotenv import load_dotenv
load_dotenv()

import os
import sys

sender_email = "jgrimes112003@gmail.com"
# receiving_emails = ["ashlyc0617@gmail.com", "jagprg@gmail.com", "jagredskin@yahoo.com", "megan92006@icloud.com", "jgrimes112003@gmail.com"]
receiving_emails = ["ashlyc0617@gmail.com", "jagprg@gmail.com", "jgrimes112003@gmail.com"]
# receiving_emails = ["jgrimes112003@gmail.com"]
def prepare_email(subject, body):
  msg = """From: %s
To: %s
Subject: %s

%s""" % (sender_email, ", ".join(receiving_emails), subject, body)
  return msg

def send_email(msg=""):
  sender_password = os.getenv("EMAIL_PASS")

  smtp_server = "smtp.gmail.com"
  smtp_port = 587
  try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
  
    server.login(sender_email, sender_password)
  
    server.sendmail(from_addr=sender_email, to_addrs=receiving_emails, msg=msg.encode("utf-8"))
    server.quit()
  
    print("Email send successfully")

  except Exception as e:
    print("Can't send email because of", e)

if __name__ == "__main__":
  msg = prepare_email(sys.argv[1], " ".join(sys.argv[2:]))
  # print(msg)
  send_email(msg)
