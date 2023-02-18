sayac = int(input("kaç ürün girmek istiyorsun : "))

urunler = []

i = 0  
while i < sayac : 
    isim = input(f"{i+1}. ürün ismi giriniz : ")
    fiyat = int(input(f"{i+1}. ürün fiyatını giriniz : "))    
    urunler.append({
        'name':isim,
        'price':fiyat
    })
    i += 1

j = 0  
while j < sayac :    
    print(f"{j+1}. ürün ismi : {urunler[j]['name']}, ürün fiyatı : {urunler[j]['price']}")
    j += 1


