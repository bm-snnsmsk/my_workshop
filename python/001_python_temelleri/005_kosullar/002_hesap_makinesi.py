islem = input("işlem seç Toplama:1 - Çıkarma:2 - Çarpma:3 - Bölme:4 : ")
sayi1 = int(input("sayi 1 : "))
sayi2 = int(input("sayi 2 : "))

if islem == "1" :
    sonuc = int(sayi1) + int(sayi2)
    print("sonuc : ",str(sonuc))
elif islem =="2" :
    sonuc = int(sayi1) - int(sayi2)
    print("sonuc : ",str(sonuc))    
elif islem =="3" :
    sonuc = int(sayi1) * int(sayi2)
    print("sonuc : ",str(sonuc))    
elif islem =="4" :
    sonuc = int(sayi1) / int(sayi2)
    print("sonuc : ",str(sonuc))
