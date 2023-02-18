while True :
    inp = input("(çıkmak için q'a basınız) Bir sayı giriniz : ")
    if inp.lower() == 'q' :
        break
    try :
        result = int(inp) 
        print(result)
    except ValueError :
        print("rakam giriniz ...")

