class Movie :
   
   def __init__(self, title, director, duration):
      self.title = title 
      self.director = director 
      self.duration = duration
      print("Movie objesi created")
   
   def __str__(self) :  ## string ifade döndürür
      return f"{self.title} by {self.director}"
   def __len__(self) :  # numeric
      return self.duration
     
   def __del__(self) :  # numeric
      print("film objesi silindi")
     





move = Movie("bir zamanlar anadoluda", "nuri bilge ceylan", 170)
move2 = Movie("yol", "yılmaz güney", 210)
print(str(move))
print(len(move))

del move2





