ogrenciler = {}

numara = input("numara : ")
isim = input("isim : ")
soyisim = input("soyisim : ")
telefon = input("telefon : ")

# ogrenciler[numara] = {
#     "ad" : isim,
#     "soyad" : soyisim,
#     "telefon" : telefon
# }

ogrenciler.update({
    numara : {
    "ad" : isim,
    "soyad" : soyisim,
    "telefon" : telefon
    }
})

print(ogrenciler[numara]['ad'])
print(ogrenciler[numara]['soyad'])
print(ogrenciler[numara]['telefon'])