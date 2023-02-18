import requests
import json
import datetime


""" bozulan_doviz = input("bozulan döviz türü : ")
alinan_doviz = input("alınan döviz türü : ")
miktar = int(input(f"ne kadar {bozulan_doviz} bozdurmak istiyorsunuz : "))

 """


payload = {}
headers= {"apikey": "oXnzRVZrdGFQFpB8INEb5RTdorVMJRhJ"}


## {'success': True, 'query': {'from': 'TRY', 'to': 'USD', 'amount': 10}, 'info': {'timestamp': 1668978903, 'rate': 0.053718}, 'date': '2022-11-20', 'result': 0.53718}

## tarih = datetime.datetime.fromtimestamp(result["info"]['timestamp'])


## print(tarih)




## print(result)



loop = True 
while loop : 
    print("***************************************************************")
    secim = input("1 - Dolar\n2 - Euro\n3 - Exit\nSeçim : ")
    if secim == "1" : 
        print("***************************************************************")  
        secim2 = input("1 - Dolar Al\n2 - Dolar Boz\n3 - Exit\nSeçim : ")
        if secim2 == "1" :
            dolar = int(input("Kaç dolar almak istiyorsun : "))
            api_url = "https://api.apilayer.com/exchangerates_data/convert?to=TRY&from=USD&amount="+str(dolar)
            response = requests.request("GET", api_url, headers=headers, data = payload)
            status_code = response.status_code
            result = json.loads(response.text)  
            kur = result["info"]["rate"]
            print(str(dolar) +" euro = " +str(dolar*kur) + " TL")
        elif secim2 == "2" :
            dolar = int(input("Kaç dolar bozmak istiyorsun : "))
            api_url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=TRY&amount="+str(dolar)
            response = requests.request("GET", api_url, headers=headers, data = payload)
            status_code = response.status_code
            result = json.loads(response.text)  
            kur = result["info"]["rate"]
            print(str(dolar) +" euro = " +str(dolar*kur) + " TL")
        elif secim2 == "3" :
            break
        else :
            print("yanlış seçim")
    elif secim == "2" :
        print("***************************************************************")
        secim3 = input("1 - Euro Al\n2 - Euro Boz\n3 - Exit\nSeçim : ")
        if secim3 == "1" :
            euro = int(input("Kaç euro almak istiyorsun : "))
            api_url = "https://api.apilayer.com/exchangerates_data/convert?to=TRY&from=EUR&amount="+str(euro)
            response = requests.request("GET", api_url, headers=headers, data = payload)
            status_code = response.status_code
            result = json.loads(response.text)  
            kur = result["info"]["rate"]
            print(str(euro) +" euro = " +str(euro*kur) + " TL")
        elif secim3 == "2" :
            euro = int(input("Kaç euro almak istiyorsun : "))
            api_url = "https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=TRY&amount="+str(euro)
            response = requests.request("GET", api_url, headers=headers, data = payload)
            status_code = response.status_code
            result = json.loads(response.text)  
            kur = result["info"]["rate"]
            print(str(euro) +" euro = " +str(euro*kur) + " TL")
        elif secim3 == "3" :
            break
        else :
            print("yanlış seçim")
    elif secim == "3" :
          loop = False
    else :
          print("yanlış seçim")
 