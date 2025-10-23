import smtplib, ssl
from email.message import EmailMessage
import os

APP_PASSWORD = os.getenv('PORTFOLIO_GMAIL_PASS')
APP_EMAIL = "spmportfoliowebsite@gmail.com"

def send_mail(sender, body, subject):

    host = "smtp.gmail.com"
    port = 465

    content = f"""
Email from: {sender}
{body}"""

    email_message = EmailMessage()
    email_message['Subject'] = subject
    email_message.set_content(content)

    username = APP_EMAIL
    password = APP_PASSWORD #Password is securely stored as an environment variable.

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        try:
            server.login(user=username, password=password)
        except (smtplib.SMTPAuthenticationError, smtplib.SMTPException,
                smtplib.SMTPHeloError, smtplib.SMTPNotSupportedError):
            return False

        try:
            server.sendmail(from_addr=username, to_addrs="spm.richards97@gmail.com", msg=email_message.as_string())
            return True
        except (smtplib.SMTPHeloError, smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused, smtplib.SMTPDataError, smtplib.SMTPNotSupportedError):
            return False

if __name__ == '__main__':
    print(APP_PASSWORD)