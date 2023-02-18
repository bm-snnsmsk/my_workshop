dosya=open("sinan.txt","r")
icerik = dosya.read()
dosya.close()
for i in icerik.splitlines() :#içeriği satır satır bölümler
    print(i)



        

