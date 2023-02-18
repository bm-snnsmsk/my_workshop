import json
import os

class User :
    def __init__(self, username, password, email) :
        self.username = username 
        self.password = password
        self.email = email

class UserRepository :
    def __init__(self) :
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        #load users from .json file
        self.loadUsers()

    def loadUsers(self) :
        if os.path.exists("users.json") :
            with open("users.json","r",encoding = "utf-8") as f :
                users = json.load(f)  ## to dictionary
                ## print(users)
                for i in users :
                    i = json.loads(i) ## string'ten python nesnesine
                    print(i["username"])
                    user = User(username = i["username"], password=i["password"], email=i["email"])
                    self.users.append(user)
            print(self.users)
        else :
            print("kayıt yok")

    def register(self, user : User) :
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu.")

    def login(self, username, password) : 
        for i in self.users :
            if i.username == username and i.password == password :
                self.isLoggedIn = True
                self.currentUser = i
                print("login yapıldı")
                break
        
    def logout(self) :
            self.isLoggedIn = False      
            self.currentUser = {}   
            print("çıkış yapıldı")

    def identity(self) :
            if self.isLoggedIn :
                print(f"username : {self.currentUser.username}")
            else :
                print("giriş yapılmadı")  
        

    def savetoFile(self) :
        ## class'ı önce kayıt edilebilir bir formata dönüştürmek lazım
        list = []
        for i in self.users :
            list.append(json.dumps(i.__dict__)) ## class yapısını dictionary yapısına çeviriyor
            ## ve dictionary'e çevrilen her class list[] listesine ekleniyor

        with open("users.json", "w") as f :
            json.dump(list, f)

repository = UserRepository()

while True :
    print("Menü".center(50,"*")) 
    secim = input("1 - Register\n2 - Login\n3 - Logout\n4 - Identity\n5 - Exit\n\nSeçiminiz : ")
    if secim == "1" :
        #register
        username = input("username : ")
        password = input("password : ")
        email = input("email : ")

        user = User(username = username, password = password, email = email)
        repository.register(user)
        print(repository.users) ## kayıt teyit etme

    elif secim == "2" :
        #login        
        if not repository.isLoggedIn :           
            username = input("username : ")
            password = input("password : ")
            repository.login(username, password)
    elif secim == "3" :
        #logout
        repository.logout()
    elif secim == "4" :
        #identity
        repository.identity()

    elif secim == "5" :
        break
    else :
        print("Yanlış seçim")
