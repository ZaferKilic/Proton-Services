import time
import decimal
import os
import sys
import colorama
from termcolor import colored
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import platform
import psutil
import random
import string
import ctypes


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (------------)                                  ","cyan"))
print("")
print("")
time.sleep(0.3)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (====>-------)                                  ","cyan"))
print(colored("                         KAYNAKLAR KONTROL EDİLİYOR                                  ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(1.5)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (========>---)                                  ","cyan"))
print(colored("                          KAYNAKLAR TAHSİS EDİLİYOR                                  ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(2)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (===========>)                                  ","cyan"))
print(colored("                                   BİTTİ                                  ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
clear()
print("")
time.sleep(0.05)
print("")
time.sleep(0.03)
print(colored("               ███╗░░░███╗░░███╗░░░█████╗░░█████╗░░█████╗░   ░█████╗░░█████╗░","cyan"))
time.sleep(0.03)
print(colored("               ████╗░████║░████║░░██╔══██╗██╔══██╗██╔══██╗   ██╔══██╗██╔══██╗","cyan"))
time.sleep(0.03)
print(colored("               ██╔████╔██║██╔██║░░██║░░██║██║░░██║██║░░██    ██║░░╚═╝██║░░╚═╝","cyan"))
time.sleep(0.03)
print(colored("               ██║╚██╔╝██║╚═╝██║░░██║░░██║██║░░██║██║░░██║   ██║░░██╗██║░░██╗","cyan"))
time.sleep(0.03)
print(colored("               ██║░╚═╝░██║███████╗╚█████╔╝╚█████╔╝╚█████╔    ╚█████╔╝╚█████╔╝","cyan"))
time.sleep(0.03)
print(colored("               ╚═╝░░░░░╚═╝╚══════╝░╚════╝░░╚════╝░░╚════╝░   ░╚════╝░░╚════╝░","cyan"))
time.sleep(0.03)
print("")
time.sleep(0.03)
print("")


welcome = Fore.CYAN + "Tekrar Merhaba M1000! Senin için ayarları ve temayı ayarlıyorum...\n"
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(0.5)

threads = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "CC Seti 400\n"
for char in threads:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(2)
print(Fore.LIGHTMAGENTA_EX + "400 CC Seti Başarıyla Yüklendi\n")

server = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "M1000 CC Sunucusu Bağlantısı İyi\n"
for char in server:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(1.3)
print(Fore.LIGHTMAGENTA_EX + "Bilgiler Kontrol Ediliyor...")
time.sleep(5.0)
print(Fore.LIGHTMAGENTA_EX + "Bilgiler Doğrulandı!")
time.sleep(0.5)
print(Fore.LIGHTMAGENTA_EX + "M1000 Sunucusuna Bağlanılıyor...")
time.sleep(0.5)

list1 = ["ARGENTINA", "UK", "US", "RUSSIA", "GERMANY", "ITALY", "FRANCE", "POLAND", "SPAIN", "CHINA", "JAPAN", "INDIA", "BRAZIL", "INDONESIA", "AUSTRALIA", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND",]
cntry = random.choice(list1)
ipss = '{}.{}.{}.{}'.format(*__import__('random').sample(range(0,255),4))

print(Fore.LIGHTMAGENTA_EX + "Test Sunucusu: ")
time.sleep(2)
print(Fore.LIGHTMAGENTA_EX + "İstekler " + str(cntry) + "-" + str(random.choice(range(1, 30))) + " [" + str(ipss) + "]" + " 32 Bayt Veri:")
time.sleep(2)
print(Fore.LIGHTMAGENTA_EX + "Şuradan yanıt: " + str(ipss) + ": " + "bytes=32 time=" + str(random.choice(range(1, 30))) + " TTL=55")
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "Şuradan yanıt: " + str(ipss) + ": " + "bytes=32 time=" + str(random.choice(range(1, 30))) + " TTL=55")
time.sleep(0.7)
print(Fore.LIGHTMAGENTA_EX + "Şuradan yanıt: " + str(ipss) + ": " + "bytes=32 time=" + str(random.choice(range(1, 30))) + " TTL=55")
time.sleep(0.2)
print(Fore.LIGHTMAGENTA_EX + "Şuradan yanıt: " + str(ipss) + ": " + "bytes=32 time=" + str(random.choice(range(1, 30))) + " TTL=55")
time.sleep(2)

print(Fore.LIGHTMAGENTA_EX + "Bağlandı.")

user = input(Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "Kaç Tane CC Kullanılacak?: ")
user = int(user)

start = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "CC Bilgileri Alınıyor..\n"
for char in start:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)



time.sleep(0.5)
print(Fore.LIGHTMAGENTA_EX + "CC Alımı Başlıyor...")
time.sleep(1.5)

print("")
print("")


def get_random_string(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    son_str = ''.join(random.choice(letters) for i in range(4))
    cvv_str = ''.join(random.choice(letters) for i in range(3))
    print(Fore.WHITE + "[" + Fore.CYAN + "M1000 CC" + Fore.WHITE + "]" + "  CC NO: " + Fore.LIGHTRED_EX + result_str + "-" + son_str + "-" + cvv_str + Fore.WHITE + "  [" + "SONUÇ: " + Fore.RED + "BAŞARISIZ" + Fore.WHITE + "]")

for i in range(user):
    get_random_string(16)
    time.sleep(0.1)
    
winner = decimal.Decimal(random.randrange(20, 250))/100

letters = string.ascii_uppercase + string.digits
heheha = ''.join(random.choice(letters) for i in range(16))
son_str = ''.join(random.choice(letters) for i in range(4))
cvv_str = ''.join(random.choice(letters) for i in range(3))

def get_random_win(length):
    print(Fore.WHITE + "[" + Fore.CYAN + "M1000 CC" + Fore.WHITE + "]" + "  CC NO: " + Fore.LIGHTGREEN_EX + str(heheha) +"-"+son_str+"-"+cvv_str+ Fore.WHITE + "  [" + "SONUÇ: " + Fore.GREEN + "BAŞARILI" + Fore.WHITE + "]")
    threads = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "CC Seti Şifresi Çözülüyor..."
    for char in threads:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    animation = "|/-\\ "
    for i in range(40):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("")
    print(Fore.WHITE + "[" + Fore.CYAN +"M1000 CC" + Fore.WHITE + "]" + "  CC NO: " + Fore.LIGHTGREEN_EX + "5319251816385726 - 06/27 - 587"+ Fore.WHITE + "  [" + "SONUÇ: " + Fore.GREEN + str(winner) + "  BAŞARILI" + Fore.WHITE + "]")

time.sleep(0.3)

get_random_win(16)

time.sleep(0.5)


print("")
print("")
time.sleep(1)
print(Fore.WHITE + "[" + Fore.CYAN + "M1000 CC" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + "CC BİLGİLERİ KAYDEDİLDİ" + Fore.WHITE + "  [" + "SONUÇ: " + Fore.GREEN + "SUCCESS" + Fore.WHITE + "]") 
time.sleep(1)

fp = open('results.txt', 'w')
fp.write(heheha + ": " + "5319 2518 1638 5726 - 06/27 - 587" + ": " + str(winner))
fp.close()

print("")
print(Fore.CYAN + "M1000 CC KAPATILIYOR...")
time.sleep(1)

closing = Fore.CYAN + "M1000 CC - 2022"
for char in closing:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.07)

time.sleep(1)
print(Fore.RESET)