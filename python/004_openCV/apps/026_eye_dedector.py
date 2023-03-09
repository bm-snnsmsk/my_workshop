import cv2

img = cv2.imread("images/avatar4.png")  ## 1.1, 2 yüz algıandı ; gözler bulunamadı
img = cv2.imread("images/gurultulu_resim.jpg")  ## ok ; gözler bulunamadı
img = cv2.imread("images/gurultulu_3.jpg") ## ok ; gözler bulunamadı
img = cv2.imread("images/ph.jpg") ## bulunamadı ; eyes bulunamadı
img = cv2.imread("images/insanlar.png") ## 1.1, 2 ile tüm yüzler bulundu ; eyes bulunamadı
img = cv2.imread("images/insanlar2.png") ## 1.2,2 ile tüm yüzler bulundu; daha küçük değerlerde ektra görüntüler de yüz olarak algılandı
img = cv2.imread("images/insanlar4.png") ## 1.3 ölçeğinde ve 3 alg ile 10 yüzden 1 tanesi bulunamadı; ama 1.3 ölçek ve 1 alg ile tüm yüzler bulundu ama gözler bulunamadı
img = cv2.imread("images/insanlar3.png") ## 1.3,1 ile 15 yüzden 11' bulundu; 1.1,1 ile 15 yüzden 13'ü bulundu ; eyes bulunamadı
img = cv2.imread("images/insanlar5.png") ## yüzler bulunamadı ; eyes bulunamadı
img = cv2.imread("images/insanlar6.png")  ## ok ; eyes = 1.3, 1
img = cv2.imread("images/portre.png")  ## ok
img = cv2.imread("images/portre2.png")  ## ok

face_cascade = cv2.CascadeClassifier("haars_cascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haars_cascades/haarcascade_eye.xml")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, 1.3, 3) 

for (x,y,w,h) in faces :
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 4)
    roi = gray_img[y:y+h, x:x+w] 
    eyes = eye_cascade.detectMultiScale(roi, 1.3, 3) 
    for (x1,y1,w1,h1) in eyes :
        cv2.rectangle(img, (x+x1,y+y1), (x+x1+w1, y+y1+h1), (0,255,0), 2)
    

cv2.imshow("Sonuc", img)

cv2.waitKey(0)
cv2.destroyAllWindows()






 