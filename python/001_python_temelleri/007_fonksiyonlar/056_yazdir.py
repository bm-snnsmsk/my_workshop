def yazdir(text, count = 1) :
    for i in range(count) :
        print(text)  


message = input("Bir mesaj yaz : ")
count = int(input("Mesajınız kaç kere yazılsın ? : "))

yazdir(message, count)


