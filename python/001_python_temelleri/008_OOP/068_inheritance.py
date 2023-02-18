class Person :
   address = "no information" 
   def __init__(self, name, age):
      self.name = name 
      self.age = age
      print("person created")
   def who_i_am(self) :
      return "I am a person"

class Student(Person) :
   def __init__(self, a, b, number):
      Person.__init__(self, a, b)
      self.number = number 
      print("student created")
   #  override
   def who_i_am(self) :
      return "I am a Student"

class Teacher(Person) :
   def __init__(self, a, b, branch):
      super().__init__(a, b)
      self.branch = branch 
      print("Teacher created")
   #  override
   def who_i_am(self) :
      return "I am a teacher"



s1= Student("sinan", 25, 202132049)
t1= Teacher("baran", 2, "computer")
print("----------------------")

print(f"isim {s1.name}, yas : {s1.age}, öğrenci no : {s1.number}, kimim ben : {s1.who_i_am()}")
print(f"isim {t1.name}, yas : {t1.age}, branş : {t1.branch}, kimim ben : {t1.who_i_am()}")


