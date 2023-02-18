x = "global x"
def func() : 
    x = "local x"         
    return x  

print(x) 
print(func()) 

''' başka bir fonksiyon '''

name = "sinan"
def change_name(n) : 
    name = n         
    return name 

print(change_name("baran")) 
print(name) 

''' başka bir fonksiyon '''

txt = "bilgisayar mühendisliği"
def change_txt() :
    global txt   
    return 'txt : '+ txt 

print(change_txt()) 
print(txt) 