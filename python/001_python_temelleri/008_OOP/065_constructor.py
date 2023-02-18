class Person :
   address = "no information" 
   def __init__(self, name, age): # self objeyi temsil ediyor this de olabilir
      self.name = name
      self.age = age
      print(f"constructor {name} için çalıştı")

p1 = Person('sinan',37)
p2 = Person('tuba',6)

print(f"isim {p1.name}, yaş : {p1.age}, {p1.address}")
p1.address = "Cudi mahallesi 61 cadde"
print(f"isim {p1.name}, yaş : {p1.age}, {p1.address}")
   

