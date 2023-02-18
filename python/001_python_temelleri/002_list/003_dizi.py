a_sinifi = ['emine', 'tubanur']
b_sinifi = ['sinan', 'baran']
isim = input("isim giriniz : ")
if isim in a_sinifi :
    print(isim,", a sınıfındadır")
elif isim in b_sinifi :
    print(isim,", b sınıfındadır")
else :
    print(isim,", herhangi bir sınıfa ait değildir")
