from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def createMessage(sender, destination, subject, body, type='plain'):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = destination
    msg['Subject'] = subject
    mailBody = body
    messageMIME = MIMEText(mailBody, type)
    msg.attach(messageMIME)
    return msg.as_string()
