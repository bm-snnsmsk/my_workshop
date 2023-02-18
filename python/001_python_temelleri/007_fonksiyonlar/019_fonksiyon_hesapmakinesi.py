def hesap_makinesi(sayi1, sayi2,islem) :
    if islem == 1 :
        return sayi1 + sayi2
    elif islem == 2 :
        return sayi1 - sayi2
    elif islem == 3 :
        return sayi1 * sayi2
    elif islem == 4 :
        return sayi1 / sayi2
    else :
        return 0    

print(hesap_makinesi(15,20,1))

        

