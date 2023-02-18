#############################################

def my_decoratif(func) :
    def wrapper(name) :
        print("önce ")
        func(name)
        print("sonra")
    return wrapper


## 2. yöntem
@my_decoratif
def greeting(name) :
    print("say greeting - " + name) 

greeting("sinan ")