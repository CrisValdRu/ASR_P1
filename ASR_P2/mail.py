import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Evidencia 3'
    msg['From'] = 'cefriasm@gmail.com'
    msg['To'] = 'tanibet.escom@gmail.com'

    text = MIMEText("Grupo 4CM1 - Equipo 4")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    sender = "cefriasm@gmail.com"
    smtp_server_name = 'smtp.gmail.com'
    port = '587'

    if port == '465':
        s = smtplib.SMTP_SSL('{}:{}'.format(smtp_server_name, port))
    else:
        s = smtplib.SMTP('{}:{}'.format(smtp_server_name, port))
        s.starttls()
    
    s.login(sender, 'RedesSensuales')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

