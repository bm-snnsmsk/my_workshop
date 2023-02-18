def yas_hesapla(dogum_yili) :
    return 2022 - dogum_yili

def emeklilik(dogum_yili) :
    ''' doğum yılına göre emeklilik yaşı hesaplama '''
    yas = yas_hesapla(dogum_yili)
    emeklilik = 65 - yas
    if emeklilik > 0 :
        print(f"Emekliliğinize {emeklilik} yıl kaldı")
    else :
        print(f"Emeklisiniz")

yas = int(input("Doğum yılınızı giriniz : "))
#emeklilik(yas)
print(help(emeklilik))
        

