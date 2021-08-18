from kayıt import *

print("""********************************************************************




Servis Kayıt Programına Hoşgeldiniz.

İşlemler:

1-Kayıtları Göster

2-Kayıtları Sorgula

3-Kayıt Ekle

4-Kayıt Sil

5-Ücret Hesapla







********************************************************************""")

kayıt = kayıt()

while True:
    işlem = input("Yapacağınız İşlemi Seçin:")

    if (işlem == "q"):
        print("Program sonlandırılıyor....")
        break
    elif (işlem == "1"):
        kayıt.kayıtları_göster()

    elif (işlem == "2"):
        isim = input("Öğrenci isimini giriniz:")
        print("kayıt sorgulanıyor.")
        kayıt.kayıt_sorgula(isim)

    elif (işlem == "3"):
        isim = input("Öğrenci isimi:")
        soyisim = input("Öğrenci Soyisimi:")
        sınıf = int(input("Sınıf:"))
        adres = input("Adres:")
        veli_numarası = int(input("Veli Numarası:"))
        kilometre = int(input("Ev ile okul arasındaki mesafeyi giriniz:"))



        yeni_öğrenci = öğrenci(isim,soyisim,sınıf,adres,veli_numarası,kilometre)

        print("kayıt ekleniyor...")

        kayıt.kayıt_ekle(yeni_öğrenci)

        print("kayıt eklendi...")



    elif (işlem == "4"):


        isim = input("Hangi öğrenciyi silmek istiyorsunuz?")

        cevap = input("Eminseniz E değilseniz H tuşuna basınız:")

        if (cevap == "E"):
            print("kayıt siliniyor...")
            kayıt.kayıt_sil(isim)
            print("kayıt silindi...")


    elif (işlem == "5"):
        kayıt.ücret_hesaplama()
