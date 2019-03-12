
import smtplib
from getpass import getpass
from email.mime.text import MIMEText

def sendMailTo(receiver, variable):
    sender = "cefriasm@gmail.com"
    content = "El " + variable + " ha excedido los limites permitidos"
    msg = MIMEText(content)
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = "Administración De Fallas  - Redes"
    smtp_server_name = 'smtp.gmail.com'
    port = '587'

    if port == '465':
        server = smtplib.SMTP_SSL('{}:{}'.format(smtp_server_name, port))
    else:
        server = smtplib.SMTP('{}:{}'.format(smtp_server_name, port))
        server.starttls()
    server.login(sender, 'RedesSensuales')
    server.send_message(msg)
    server.quit()
    return;

sendMailTo("cefriasm@gmail.com", "Uso de CPU")
sendMailTo("castilloreyesjuan@gmail.com", "Uso de CPU y mujerzuelas")
sendMailTo("cefriasm@gmail.com", "Uso del Gran cesar")