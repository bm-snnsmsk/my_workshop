#############################################

def my_decoratif(func) :
    def wrapper() :
        print("önce ")
        func()
        print("sonra")
    return wrapper



## 1. yöntem 
def sayhello() :
    print("say hello") 

sayhello = my_decoratif(sayhello)
sayhello()


## 2. yöntem
@my_decoratif
def greeting() :
    print("say greeting") 

greeting()