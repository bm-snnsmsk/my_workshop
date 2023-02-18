import datetime

tarih = input("Aracınızın Trafiğe çıkış tarihi : ")
tarih = tarih.split("/")
tarihObject = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))

fark = datetime.datetime.now() - tarihObject
print(fark)
print(f"Aracınız {fark.days} gündür trafiktedir ve {fark.days//360}. servis aralığındadır ")