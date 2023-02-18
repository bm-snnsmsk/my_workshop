'''  1. yol  list() ile yazdırma '''
def square(sayi) :          
    return sayi ** 2  

numbers = [1,3,5,7,9,11]

print(list(map(square, numbers)))

'''  2. yol  for döngüsü ile yazdırma '''
for i in map(square, numbers) :
    print(i)


'''  3. yol  lambda '''

print(list(map(lambda n : n ** 2, numbers)))



'''  4. yol  lambda '''
lmbd = lambda n : n ** 2
print(list(map(lmbd, numbers)))


