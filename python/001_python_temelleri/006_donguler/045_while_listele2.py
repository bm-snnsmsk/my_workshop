baslangic = int(input("başlangıç sayısı gir : "))
bitis = int(input("bitiş sayısı gir : "))

while baslangic <= bitis :
    if baslangic % 2 != 0 :
        print(baslangic)
    baslangic += 1