sayac = int(input("kaç sayı girmek istiyorsun : "))

liste = []
i = 0
while i < sayac :
    elem = int(input(f"{i+1}. sayi gir : "))
    liste.append(elem)
    i += 1

liste.sort()
j = 0
while j < len(liste) :
    print(liste[j])
    j += 1 