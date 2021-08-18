import sqlite3
import math
import time

class öğrenci():


    def __init__(self,isim,soyisim,sınıf,adres,veli_numarası,kilometre):
        self.isim = isim
        self.soyisim = soyisim
        self.sınıf = sınıf
        self.adres = adres
        self.veli_numarası = veli_numarası
        self.kilometre = kilometre




    def __str__(self):

        return "Öğrenci isimi: {}\nÖğrenci Soyisimi: {}\nSınıfı: {}\nAdresi: {}\nVeli Numarası: {}\nKilometre: {}\n".format(self.isim,self.soyisim,self.sınıf,self.adres,self.veli_numarası,self.kilometre)


class kayıt():

    def __init__(self):
        self.bağlantı_oluştur()

    def bağlantı_oluştur(self):

        self.bağlantı = sqlite3.connect("kayıt.db")

        self.cursor = self.bağlantı.cursor()

        sorgu = "create table if not exists kayıtlar(isim TEXT, soyisim TEXT, sınıfı INT, adres TEXT, veli_numarası INT, kilometre INT)"

        self.cursor.execute(sorgu)

        self.bağlantı.commit()

    def bağlantıyı_kes(self):

        self.bağlantı.close()

    def kayıtları_göster(self):

        sorgu = "Select * From kayıtlar"

        self.cursor.execute(sorgu)

        kayıtlar = self.cursor.fetchall()

        if (len(kayıtlar) == 0):
            print("kayıtlar inceleniyor...")
            time.sleep(1)
            print("kayıt bulunmuyor.")

        else:
            for i in kayıtlar:
                kayıt = öğrenci(i[0],i[1],i[2],i[3],i[4],i[5])
                print(kayıt)


    def kayıt_sorgula(self,isim):

        sorgu = "Select * From kayıtlar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kayıtlar = self.cursor.fetchall()

        if (len(kayıtlar) == 0):
            print("kayıtlar inceleniyor...")
            time.sleep(1)
            print("kayıt bulunmuyor.")

        else:
            kayıt = öğrenci(kayıtlar[0][0],kayıtlar[0][1],kayıtlar[0][2],kayıtlar[0][3],kayıtlar[0][4],kayıtlar[0][5])
            print(kayıt)

    def kayıt_ekle(self,öğrenci):

        sorgu = "INSERT into kayıtlar Values(?,?,?,?,?,?)"

        self.cursor.execute(sorgu,(öğrenci.isim,öğrenci.soyisim,öğrenci.sınıf,öğrenci.adres,öğrenci.veli_numarası,öğrenci.kilometre))

        self.bağlantı.commit()

    def kayıt_sil(self,isim):

        sorgu = "Delete From kayıtlar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.bağlantı.commit()

    def ücret_hesaplama(self,isim):

        sorgu = "Select * From kayıtlar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kayıtlar = self.cursor.fetchall()

        if (len(kayıtlar) == 0):
            print("kayıtlar inceleniyor...")
            time.sleep(1)
            print("kayıt bulunmuyor.")

        else:
            kayıt = öğrenci(kayıtlar[0][0], kayıtlar[0][1], kayıtlar[0][2], kayıtlar[0][3], kayıtlar[0][4],kayıtlar[0][5])
            print(kayıt)

            kilometre = int(input("okul ile ev arasındaki kilometreyi giriniz:"))

            if (kilometre >= 0 and kilometre <= 1):
                print("Servis ücretiniz: 311,65 Türk Lirası.")

            elif (kilometre >= 1 and kilometre <= 3):
                print("Servis Ücretiniz: 341,55 Türk Lirası.")

            elif (kilometre >= 3 and kilometre <= 5):
                print("Servis Ücretiniz: 370,30 Türk Lirası.")

            elif (kilometre >= 5 and kilometre <= 7):
                print("Servis ücretiniz: 385,25 Türk Lirası.")

            elif (kilometre >= 7 and kilometre <= 9):
                print("Servis Ücretiniz: 405.95 Türk Lirası.")

            elif (kilometre >= 9 and kilometre <= 11):
                print("Servis Ücretiniz: 470.35 Türk Lirası.")

            elif (kilometre >= 11 and kilometre <= 13):
                print("Servis Ücretiniz: 541.65 Türk Lirası.")

            elif (kilometre >= 13 and kilometre <= 15):
                print("Servis Ücretiniz: 569.25 Türk Lirası.")

            elif (kilometre >= 15):
                print("Tarife dışı bir ücret girdiniz. Yetkililere danışınız.")

            else:
                print("Tanımlanamayan bir sayı girdiniz.")