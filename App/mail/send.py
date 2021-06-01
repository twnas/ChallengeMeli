import ssl
import smtplib

def sendEmail(dadosEmail, messageString):
    context = ssl.create_default_context()

    with smtplib.SMTP(dadosEmail['smtp_server'], dadosEmail['port']) as server:
        server.starttls(context=context)
        server.login(dadosEmail['sender_email'], dadosEmail['password'])
        server.sendmail(dadosEmail['sender_email'], dadosEmail['receiver_email'],"Alta Seguridad")

    print ("######################### Correo Enviado ###############################")
    print(messageString)
