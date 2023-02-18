'''  1. yol  list() ile yazdırma '''
def check_even(sayi) :          
    return sayi % 2 == 0  

numbers = [1,2,3,4,5,6,7,8,9,10,11]

print(list(filter(check_even, numbers)))

'''  2. yol  lambda '''

print(list(filter(lambda n : n % 2 == 0, numbers)))



'''  3. yol  lambda '''
lmbd = lambda n : n % 2 == 0
print(list(filter(lmbd, numbers)))


