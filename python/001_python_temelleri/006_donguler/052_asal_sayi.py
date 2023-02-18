isAsal = True
while isAsal :
    sayi = int(input("bir sayi gir : "))
    if sayi >= 2 : 
        for i in range(2, sayi // 2, 1) :
            if sayi % i == 0 :
                isAsal = False 
    else :
        isAsal = False 
    if isAsal : 
        print(f"{sayi}, sayısı asal sayıdır..")
    else :
         print(f"{sayi}, sayısı asal değildir..")