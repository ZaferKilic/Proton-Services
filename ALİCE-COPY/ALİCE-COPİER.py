import os,getpass
from path import Path

USER_NAME = getpass.getuser()
if os.path.isdir("SECRET"):
    pass
else:
    os.mkdir("SECRET")
HEDEF = 'SECRET'

try:
    bat_path_desktop = r"C:/Users/{}/Desktop".format(USER_NAME)
    KAYNAK = bat_path_desktop 
    k = Path(KAYNAK)
    h = Path(HEDEF)
    def transfer():
        print ("\nDosyalar %s adresinden %s adresine kopyalanıyor !" % (k, h))
        dosya_sayisi = 0
        for i in k.walkfiles(): 
                dosya_sayisi += 1
                i.copy(h) 
        if (dosya_sayisi == 0):
            print("Mevcut dizinde amaç dosya bulunamadı.")
        else:
            print("\n%s adet dosya başarılı şekilde kopyalandı" % dosya_sayisi)
    if __name__ == "__main__":
        if(os.path.exists(KAYNAK)):
            transfer()
        else:
            print("\n\nDosya Yolu Bulunamadı")
except:
    pass
try:
    bat_path_desktop = r"C:/Users/{}/Documents".format(USER_NAME)
    KAYNAK = bat_path_desktop 
    k = Path(KAYNAK)
    h = Path(HEDEF)
    def transfer():
        print ("\nDosyalar %s adresinden %s adresine kopyalanıyor !" % (k, h))
        dosya_sayisi = 0
        for i in k.walkfiles(): 
                dosya_sayisi += 1
                i.copy(h) 
        if (dosya_sayisi == 0):
            print("Mevcut dizinde amaç dosya bulunamadı.")
        else:
            print("\n%s adet dosya başarılı şekilde kopyalandı" % dosya_sayisi)
    if __name__ == "__main__":
        if(os.path.exists(KAYNAK)):
            transfer()
        else:
            print("\n\nDosya Yolu Bulunamadı")
except:
    pass
try:
    bat_path_desktop = r"C:/Users/{}/Downloads".format(USER_NAME)
    KAYNAK = bat_path_desktop 
    k = Path(KAYNAK)
    h = Path(HEDEF)
    def transfer():
        print ("\nDosyalar %s adresinden %s adresine kopyalanıyor !" % (k, h))
        dosya_sayisi = 0
        for i in k.walkfiles(): 
                dosya_sayisi += 1
                i.copy(h) 
        if (dosya_sayisi == 0):
            print("Mevcut dizinde amaç dosya bulunamadı.")
        else:
            print("\n%s adet dosya başarılı şekilde kopyalandı" % dosya_sayisi)
    if __name__ == "__main__":
        if(os.path.exists(KAYNAK)):
            transfer()
        else:
            print("\n\nDosya Yolu Bulunamadı")
except:
    pass