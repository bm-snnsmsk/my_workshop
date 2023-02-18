############# bankamatik
hesapA = {
    'ad':'sinan şimşek',
    'hesapNo':'132546',
    'bakiye':3000,
    'ekhesap':2000
}

hesapB = {
    'ad':'Baran şimşek',
    'hesapNo':'1324157',
    'bakiye':13000,
    'ekhesap':20000
}
''' referans tipler olduğu için  değerlerde güncellenme yapılabilir'''



def para_cek(hesap, miktar) :
    print(f'Merhaba {hesap["ad"]}')
    if hesap['bakiye'] >= miktar :
        hesap['bakiye'] -= miktar
        bakiye_sorgula(hesap)
    else :
        resp = input(f'Sayın {hesap["ad"]}, bakiyeniz yetersiz. Ek hesap kullanmak ister misiniz ? (e / h) : ') 
        if resp.lower() == 'e' :
            kullanilabilirBakiye = hesap['bakiye'] + hesap['ekhesap']
            if kullanilabilirBakiye >= miktar :
                hesap['ekhesap'] -= (miktar - hesap['bakiye'] )
                hesap['bakiye']  = 0
                bakiye_sorgula(hesap)
            else : 
                print("Bakiyeniz yetersiz")
                bakiye_sorgula(hesap)

def bakiye_sorgula(hes) :    
    print(f"Bakiyeniz : {hes['bakiye']}")
    print(f"ekhesap bakiiyeniz : {hes['ekhesap']}")



para_cek(hesapA, 2500)
para_cek(hesapA, 2500)