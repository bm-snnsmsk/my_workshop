deger = input("sayi veya metin giriniz : ")
uzunluk = list(deger)
rakam_sayac = 0
harf_sayac = 0
for i in uzunluk :
      if str(i).isdecimal() :
        rakam_sayac+=1
      else :
        harf_sayac+=1
print(uzunluk)
print(deger," inputu içinde ; ",rakam_sayac," adet rakam ve ",harf_sayac," adet harf bulunmaktadır")
            


        

