import smtplib
from email.mime.text import MIMEText


def send_email(recipient, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email_address'
    msg['To'] = recipient

    # Connect to the email server and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email_address', 'your_email_password')
    server.send_message(msg)
    server.quit()
