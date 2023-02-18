isim = input("isminiz : ")
yas = int(input("Yaşınız : "))
egitim = input("eğitim durumunuz : ")


if yas >= 18 and (egitim == 'lise' or egitim == 'universite') :
    print(f"Sayın {isim}, Ehliyet alabilirsiniz")
else  :
    print(f"Sayın {isim},ehliyet için yasınız veya eğitim durumunuz uygun değil")