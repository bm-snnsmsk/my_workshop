import cv2
import numpy as np

## sesler ve videoalar gibi büyük boyutlu datalar (sıkıştırılarak gönderilir) gönderilirken encode edilir, karşıdan alındığında decode edilerek alınır

cam = cv2.VideoCapture(0)

width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)) ## kamera genişliğini al
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)) ## kamera yüksekliğini al
print(width, height)
fourcc = cv2.VideoWriter_fourcc(*"MP4V") ## encode işlemi (*'XVID') = .avi
out = cv2.VideoWriter("images/kamera.mp4", fourcc, 30, (width, height)) ## FPS = saniyelik görüntü sayısı

while True : ## cam.isOpened() 'da olabilir
    ret, frame = cam.read()  
    if not ret :
        print("Kameradan görüntü alınamadı") 
        break
    out.write(frame)
    cv2.imshow("Kamera", frame)
    if cv2.waitKey(25) & 0XFF == ord('q') :
        print("Kayıt sonlandırıldı")
        break

cam.release() ##yazma işleminin de serbest bırakılması lazım, bu kod olmazsa, kamera hala çalışıyor görünecek arka planada ve görüntü ile ilgili bir işlem yapılamaz
out.release() ##yazma işleminin de serbest bırakılması lazım, bu kod olmazsa, kamera hala çalışıyor görünecek arka planada ve görüntü ile ilgili bir işlem yapılamaz
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 