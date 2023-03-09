import cv2
import numpy as np


kamera = cv2.VideoCapture(0) 
while True :
    ret, goruntu = kamera.read()

    ## bu şekiller döngünün içinde olack ki görüntü olduğu sürece bu şekiller de çıksın START
    cv2.rectangle(goruntu, (100,200), (300,50), (25,36,98), 2) ## rectangle_oluşacak goruntunun_içinde_çıksın, start_point(x,y), finish_point(x,y), color(BGR), kalınlık
    cv2.line(goruntu, (500,200), (300,50), (150,36,98), 3) ## line_oluşacak goruntunun_içinde_çıksın, start_point(x,y), finish_point(x,y), color(BGR), kalınlık
    cv2.circle(goruntu, (200,350), (50), (150,250,98), 4) ## circle_oluşacak goruntunun_içinde_çıksın, center_point(x,y), redius, color(BGR), kalınlık
    cv2.putText(goruntu, "Sinan Simsek", (0, 50), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0), 2) ## text_oluşacak goruntunun_içinde_çıksın, start_point(x,y(sol-alt)), font, font_size, color(BGR), kalınlık
    ## bu şekiller döngünün içinde olack ki görüntü olduğu sürece bu şekiller de çıksın END

    cv2.imshow("Kamera", goruntu)
    if cv2.waitKey(30) & 0XFF == ord('q') : ## döngü 30 milisaniyede bir resim alıyor ve bu 30 milisaniyede olduğu için akıcı bir videoya dönüşüyor
        break
kamera.release()
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 