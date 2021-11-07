# sends mail

import json 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def senMail(frEmail,toEmail,pwd,subj,message):
    msg = MIMEMultipart() 
    msg['From'] = frEmail 
    msg['To'] = toEmail
    msg['Subject'] = subj

    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], pwd)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
