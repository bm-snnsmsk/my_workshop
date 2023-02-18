class Circle :
   pi = 3.14
   def __init__(self, r): 
      self.r = r
   
   def cevre_hesapla(self) :
      return 2 * self.r * self.pi
   def alan_hesapla(self) :
      return (self.r ** 2) * self.pi

c1 = Circle()
c2 = Circle(5)

print(f"alan {c1.cevre_hesapla()}, cevre : {c1.alan_hesapla()}")
print(f"alan {c2.cevre_hesapla()}, cevre : {c2.alan_hesapla()}")

