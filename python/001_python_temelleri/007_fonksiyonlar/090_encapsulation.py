## encapsulation 
def outer(x) :
    def inner() :
        return x + 1
    y = inner()
    print(x, y)

outer(10) 

## encapsulation 
def fact(x) :
    if not isinstance(x, int) :
        raise TypeError("geçersiz değer")
    if not x >= 0 :
        raise ValueError("sayı 0 veya 0'dan büyük olmalı")
    def inner(x) :
        if x <= 1 :
            return 1
        else :
            return x * inner(x - 1)
    return inner(x)

try :
    print(fact("-5")) 
except Exception as e :
    print(e)

## asasas
def usalma(taban) :
    def inner(us) :
        return taban ** us
    return inner

a = usalma(2)
print(a(3))

