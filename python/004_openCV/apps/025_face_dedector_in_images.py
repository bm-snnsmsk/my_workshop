import cv2
import matplotlib.pyplot as plt



img = cv2.imread("images/avatar4.png")  ## bulunamadı (avatar!)
img = cv2.imread("images/gurultulu_resim.jpg")  ## ok
img = cv2.imread("images/gurultulu_3.jpg") ## ok
img = cv2.imread("images/ph.jpg") ## bulunamadı
img = cv2.imread("images/insanlar.png") ## 1.1, 2 ile tüm yüzler bulundu
img = cv2.imread("images/insanlar2.png") ## 1.2,2 ile tüm yüzler bulundu; daha küçük değerlerde ektra görüntüler de yüz olarak algılandı
img = cv2.imread("images/insanlar3.png") ## 1.3,1 ile 15 yüzden 11' bulundu; 1.1,1 ile 15 yüzden 13'ü bulundu
img = cv2.imread("images/insanlar4.png") ## 1.3 ölçeğinde ve 3 alg ile 10 yüzden 1 tanesi bulunamadı; ama 1.3 ölçek ve 1 alg ile tüm yüzler bulundu
img = cv2.imread("images/insanlar5.png") ## yüzler bulunamadı
img = cv2.imread("images/insanlar6.png")  ## ok
img = cv2.imread("images/portre.png")  ## ok
img = cv2.imread("images/portre2.png")  ## ok

face_cascade = cv2.CascadeClassifier("haars_cascades/haarcascade_frontalface_default.xml")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 1.3, 3) ## img, ölçek, arama_matrixi_algoritma( = en az üç düktürtgende bir yüz keşfedilirse sonucu true olarak döndür)
print(faces) ## yüzün bulunduğu diktörtgenin sol-üst(x ve y) değerleri ve bulunan dikdörtgenin w ve h

for (x,y,w,h) in faces :
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 4)






cv2.imshow("Sonuc", img)

# plt.figure(figsize=(12,8))
# plt.imshow(gray_img, cmap="gray")
# plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()






 