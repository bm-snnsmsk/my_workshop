#############################################
def usalma(taban) :
    def inner(us) :
        return taban ** us
    return inner

a = usalma(2) 
print(a(3))

##############################################

def yetki_sorgula(page) :
    def inner(role) :
        if role == 'admin' :
            return "{0} rolü {1} sayfasına ulaşabilir".format(role, page)
        else :
            return "{0} rolü {1} sayfasına ulaşamaz".format(role, page)
    return inner

user1 = yetki_sorgula('home') 
user2 = yetki_sorgula('siparişler') 
print(user1("admin"))
print(user1("kullanici"))

#############################################

def islem(islem_adi) :
    ## toplama
    def toplam(*args) :
        result = 0
        for i in args :
            result += i
        return result

    ## toplama
    def carpma(*args) :
        result = 1
        for i in args :
            result *= i
        return result

  
    if islem_adi == 'toplama' :
        return toplam 
    else :
        return carpma 

toplama = islem("toplama") 
print(toplama(2,5,7,1))
carpma = islem("carpma") 
print(carpma(2,5,7,1))




