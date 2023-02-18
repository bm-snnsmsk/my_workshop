#############################################
import time
import math

## 1. yöntem
def factoriyel(n) :
    start = time.time() 
    time.sleep(1)
    print(math.factorial(n))
    finish = time.time() 
    
    print("işlem "+str(finish - start)+" saniye sürdü")

factoriyel(15)

## 2. yöntem
def calculate_time(func) :
    def inner(*args, **kwargs) :
        start = time.time() 
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time() 
        print(func.__name__+", işlemi "+str(finish - start)+" saniye sürdü")
    return inner

@calculate_time
def usalma(a,b) :   
    print(math.pow(a,b))


usalma(5,5)