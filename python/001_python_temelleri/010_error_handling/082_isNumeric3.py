import re 
import math


def is_numeric(val) :
    val = int(val)
    if val < 0 : 
        raise Exception("geçersiz değer")
    else :
        return math.factorial(val)
   
            
inp = input("bir sayı girin : ")
try :
    val = is_numeric(inp)
    print(val)
except Exception as e :
    print(e)



