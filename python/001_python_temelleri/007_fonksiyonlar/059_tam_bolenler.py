def tam_bolen(sayi) :
    bolenler = []
    for i in range(1, sayi + 1) : 
        if sayi % i == 0 :
            bolenler.append(i)            
    return bolenler  


print(tam_bolen(15))


