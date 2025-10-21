import smtplib, ssl
import os

def send_mail(sender, body, subject):
    host = "smtp.gmail.com"
    port = 465

    username = "spm.richards97@gmail.com"
    password = os.getenv("GMAIL_PASSWORD") #Password is securely stored as an environment variable.

    context = ssl.create_default_context()
    message = f"""\
    Subject: {subject}\
{body}"""

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, sender, message)
