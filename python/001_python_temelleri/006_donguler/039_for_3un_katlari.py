sayilar = [1,2,3,5,6,9,8,7,4,15,21,24,26]

toplam = 0 
for i in sayilar :
    toplam += i
    if i % 3 == 0 :
        print(i)

print(f'toplam : {toplam}')
