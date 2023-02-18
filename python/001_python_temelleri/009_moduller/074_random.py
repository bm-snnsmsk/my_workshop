''' random '''
import random


""" for i in dir(random) :
    print(i)
 """

names = ["sinan","baran","tuba","emine", "fatma","rizgar","nujin","süleyman","kendal","özgür","firdevs","hiranur"]
name = 'sinan şimşek'

print(random.random())  # 0.0 - 1.0 arası
print(random.random() * 100)  
print(random.uniform(2, 15))   # float
print(random.randint(2, 15))   # int

print(names[random.randint(0, len(names) - 1)])   # rastgele liste elemenı seçme
print(random.choice(names))   # rastgele liste elemenı seçme

print(name[random.randint(0, len(name) - 1)])   # rastgele string karakteri seçme
print(random.choice(name))   # rastgele string karakteri seçme

random.shuffle(names) # liste elemanlarını rastgele karıştır
print(names) # listeyi yaz

print(random.sample(name, 3))   # belirtilen strinden belirtilen sayıda rastgele karakter seçer
print(random.sample(names, 3))   # belirtilen listeden belirtilen sayıda rastgele eleman seçer

