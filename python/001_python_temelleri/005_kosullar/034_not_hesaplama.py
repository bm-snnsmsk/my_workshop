vize = float(input("vize notu giriniz : "))
final = float(input("final notu  giriniz : "))

ortalama = vize * 0.3 + final * 0.7

if ortalama <=100 and ortalama > 90 :
    print(f"Ortalamanız {ortalama}, Harf Notunuz : AA")
elif ortalama <=90 and ortalama > 80 :
    print(f"Ortalamanız {ortalama}, Harf Notunuz : BA")
elif ortalama <=80 and ortalama > 70 :
    print(f"Ortalamanız {ortalama}, Harf Notunuz : BB")
elif ortalama <=70 and ortalama > 65 :
    print(f"Ortalamanız {ortalama}, Harf Notunuz : BC")
elif ortalama <=65 and ortalama > 55 :
    print(f"Ortalamanız {ortalama}, Harf Notunuz : CC")
elif ortalama <=55 and ortalama > 50 :
    print(f"Ortalamanız {ortalama}, Harf Notunuz : CD")
elif ortalama <=50 and ortalama > 45 :
    print(f"Ortalamanız {ortalama}, Harf Notunuz : DD")
else :
    print(f"Ortalamanız {ortalama}, Harf Notunuz : FF")