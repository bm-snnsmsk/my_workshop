def not_hesapla(satir) :
    liste = satir.split(":")
    ogrenci_adi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if ortalama <= 100 and ortalama >= 90 :
        harf = 'AA'
    elif ortalama < 90 and ortalama >= 85 :
        harf = 'BA'
    elif ortalama < 85 and ortalama >= 80 :
        harf = 'BB'
    elif ortalama < 80 and ortalama >= 75 :
        harf = 'CB'
    elif ortalama < 75 and ortalama >= 70 :
        harf = 'CC'
    elif ortalama < 70 and ortalama >= 65 :
        harf = 'DC'
    elif ortalama < 65 and ortalama >= 60 :
        harf = 'DD'
    elif ortalama < 60 and ortalama >= 50 :
        harf = 'FD'
    elif ortalama < 50 and ortalama >= 0 :
        harf = 'FF'
    return ogrenci_adi + " : " + harf + "\n"

    

def ortalamalari_goster() :
    with open("sinav_notlari.txt", "r", encoding = "utf-8") as file :
        content = file.read()
        for i in content.splitlines() :
            print(not_hesapla(i))

def not_gir() :
    ad = input("isim  : ")
    soyad = input("soyad  : ")
    not1 = input("not 1  : ")
    not2 = input("not 2  : ")
    not3 = input("not 3  : ")

    with open("sinav_notlari.txt", "a", encoding = "utf-8") as file :
        file.write(ad + " " + soyad + ":" + not1 + "," + not2 + "," + not3 + "\n")



def not_kaydet() :
    with open("sinav_notlari.txt", "r", encoding = "utf-8") as file :
        liste = []
        for i in file :
            liste.append(not_hesapla(i))

        with open("sonuclar.txt", "w", encoding = "utf-8") as file2 :
            for i in liste :
                file2.write(i)

isLoop  = True
while isLoop :
    islem = input("1- Notları oku : \n2-Not Gir : \n3-Notları Kaydet\n4- Çıkış\n")

    if islem == "1" :
        ortalamalari_goster()
    elif islem == "2" :
        not_gir()
    elif islem == "3" :
        not_kaydet()
    elif islem == "4" :
        isLoop = False
    else :
        print('geçersiz işlem')
        

