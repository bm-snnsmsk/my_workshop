class Person :
   address = "no information" 
   def __init__(self, name, age): # self objeyi temsil ediyor this de olabilir
      self.name = name
      self.age = age
   
   def intro(a) :
      print("inctance' i işaret eden ilk parametre (self ama herhangi bir karakter veya string ifade) parametresi tanımlanmalı --- ", a.name)
   def calculate(self) :
      return 2022 - self.age   
p1 = Person('sinan',1985)
p2 = Person('tuba',2017)

print(f"isim {p1.name}, yaş : {p1.age}, {p1.address}")
p1.address = "Cudi mahallesi 61 cadde"
print(f"isim {p1.name}, yaş : {p1.age}, {p1.address}")
p1.intro()
print(p1.name, " yasi : ",p1.calculate())
print(p2.name, " yasi : ",p2.calculate())
   

