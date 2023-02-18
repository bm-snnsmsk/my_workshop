import random
sayi = random.randint(1,100)
game = True
hak = 5
puan = 100
while game == True :
    if hak > 0 :
        tahmin = int(input(f"1-100 arası bir sayi gir : ")) 
        puan = hak * 20
        hak -= 1
        if tahmin > sayi :
            print(f"Büyük sayı girdiniz... Kalan hakkınız : {hak}")
            game = True
        elif tahmin < sayi : 
            print(f"Küçük sayı girdiniz... Kalan hakkınız : {hak}")
            game = True
        else :
            print(f"Tebrikler, doğru sayı girdiniz... Puanınız : {puan}")
            game = False
    else :
        print(f"Oyunu kaybettiniz. Doğru sayı {sayi}")
        game = False