with open("sinan.txt", "r+", encoding = 'utf-8') as file :
    liste = file.readlines()
    liste.insert(6,'muhammed şimşek\n')
    file.seek(0)


    # for i in liste :
    #     file.write(i)

    
    file.writelines(liste)



        

