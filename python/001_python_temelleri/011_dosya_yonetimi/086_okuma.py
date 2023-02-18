try : 
    file = open("sinan.txt", "r", encoding = 'utf-8')
    # print(file) # dosya ile i,lgili açıklamalr

    ## 1. okuma yöntemi
    # for i in file : 
    #     print(i)

    ## 2. okuma yöntemi
    # for j in file : 
    #     print(j, end = "")

    ## 3. yöntem
    # icerik = file.read()
    # for i in icerik.splitlines() :
    #     print(i) 

    ## 4. yöntem
    # print(file.readline(), end = "") 
    # print(file.readline(), end = "") 
    # print(file.readline(), end = "") 

    ## 5. yöntem
    icerik = file.readlines()
    print(icerik) 

    
except FileNotFoundError :
    print("Dosya okuma hatası..")
finally :
    ## print("dosya kapandı")
    file.close()




        

