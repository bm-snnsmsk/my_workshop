urunler = [
    {'name':'samsung s6', 'price':'5000'},
    {'name':'samsung s7', 'price':'7000'},
    {'name':'samsung s8', 'price':'9000'},
    {'name':'samsung s9', 'price':'11000'},
    {'name':'samsung s10', 'price':'15000'}
    ]

toplam = 0
for i in urunler :
    if (int(i['price']) <= 9000) :
        print(i['name'])

for i in urunler :
    toplam += int(i['price'])
print(toplam)
