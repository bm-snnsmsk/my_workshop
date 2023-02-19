liste = ['C:/Users/bm_snnsmsk/Desktop/my_workspace/python/music/Çilli Bom Bom (Yüz Numaralı Adam) Film Müziği.mp3', 'C:/Users/bm_snnsmsk/Desktop/my_workspace/python/music/ender_balkir_ruhumda_sizi.mp3', 'C:/Users/bm_snnsmsk/Desktop/my_workspace/python/music/gevre gevramı.mp3']


for i in range(0,len(liste)) :
    bol = liste[i].split('/')
    print(bol[len(bol) - 1])
    
