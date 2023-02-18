import re 

inp = input("bir text girin : ")

def is_turkce(text) :
    for i in text :
        if re.search('[çğıöşüÇĞİÖŞÜ]', text) :
            raise Exception("Türkçe karakter girdiniz ...")
        else : 
            raise Exception("doğru parola")
            
try :
    is_turkce(inp)
except Exception as e :
    print(e)

