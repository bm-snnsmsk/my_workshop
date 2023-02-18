for i in range(3,50,4) : # startindex, finishindex, mod
    print(i)


isim = "sinan"
for index, letter in enumerate(isim) :
    print(f"index : {index}, harf : {letter}")


liste1 = [1,2,3,4,5,7]
liste2 = ["a","b","c","d","e","f","de"]

print(list(zip(liste1, liste2)))
