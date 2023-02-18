boy = float(input("boy cm olarak giriniz : "))
kilo = float(input("kilo giriniz : "))
boy /= 100
bki = kilo / (boy ** 2)

print(bki)
if bki > 0 and bki < 18.5 :
    print("Zayıf")
elif bki >= 18.5 and bki < 25 :
    print("Normal")
elif bki >= 25 and bki < 30 :
    print("Fazla kilolu")
elif bki >= 30 :
    print("Obez")