##################################################
liste = [1,2,3,4,5]

iterator = iter(liste)

print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3
print(next(iterator)) # 4
print(next(iterator)) # 5
# print(next(iterator)) # StopIteration error

###################################################
liste2 = [10,20,30,40,50]
iterator2 = iter(liste2) 
while True :
    try :
        e = next(iterator2)
        print(e)
    except StopIteration :
        break

###################################################

class MyNumbers :
    def __init__(self, start, stop) :
        self.start = start 
        self.stop = stop 

    def __iter__(self) :
        return self 
    
    def __next__(self) :
        if self.start <= self.stop :
            x = self.start
            self.start += 1
            return x 
        else :
            raise StopIteration


liste3 = MyNumbers(33, 44)
for i in liste3 :
    print(i)


liste4 = MyNumbers(100, 110)
while True :
    try :
        e = next(iter(liste4))
        print(e)
    except StopIteration :
        break


