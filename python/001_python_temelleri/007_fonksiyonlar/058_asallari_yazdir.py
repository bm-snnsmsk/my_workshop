def asal_sayilar(a, b) :
    asallar = []
    for i in range(a,b+1) :        
        isAsal = True
        for j in range(2,i) :
            if i % j == 0 :
                isAsal = False
        if isAsal == True :
            asallar.append(i)
    return asallar  


print(asal_sayilar(5,19))


