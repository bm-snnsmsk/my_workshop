def ciftler(sayi) :
    liste = []
    for i in range(0, sayi, 1) :
        if(i % 2 == 0) :
         liste.append(i) # listeye eleman ekleme
    return liste
