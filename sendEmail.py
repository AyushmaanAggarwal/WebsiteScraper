import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def gmail_send_message(subject, message_text, path):
    with open(path + "instance/pythonpass", 'r') as file:
        email_password = file.read()

    with open(path + "instance/toEmail", 'r') as file:
        to_address = file.read()

    with open(path + "instance/fromEmail", 'r') as file:
        from_address = file.read()

    em = MIMEMultipart('alternative')
    em['From'] = from_address
    em['To'] = to_address
    em['Subject'] = subject
    part2 = MIMEText(message_text, 'html')
    em.attach(part2)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(from_address, email_password)
            smtp.sendmail(from_address, to_address, em.as_string())
        return "Email Sent!"
    except:
        return "Email failed to send"
