import cv2

## kare = videonun herhangi bir andaki resmidir
## video = birçok karenin bir araya gelmesidir

# kamera = cv2.VideoCapture(0) ## kendi pc'mize tanımlı olan kamerayı alır
# kamera = cv2.VideoCapture(1) ## USB'de tanımlı olan kamerayı alır
# kamera = cv2.VideoCapture(2) ## videoda tanımlı olan kamerayı alır

cam = cv2.VideoCapture(0) ## kamera = cv2.VideoCapture("http://192.168.0.26:8080/video") ## ama ip webcam uygulamasını indir, uygulamanın en aşağısında START SERVER tıkla, ordan çıkan ip'e /video şeklinde buraya yaz
## 2 PC'ye bağlı harici kamera

if not cam.isOpened() :
    print("kamera tanımlı değil")
    exit()
## video  == seri halde çekilen fotoğraflardır
## ret = kameranın çalışıp çalışmadığı kontrolu
## goruntü = sürekli alınacak görüntüler

print(cam.get(3)) ## camera width
print(cam.get(4)) ## camera height
print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)) ## camera height // https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
cam.set(3, 100)
cam.set(4, 100)

while True :
    ret, frame = cam.read() ## kendi kameramızı kotrol et,  kameramızdan görüntü al oku, ret = bool değer
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ## görüntü gri'ye çevrildi
    frame = cv2.flip(frame, 1) ## bu satır yazılırsa; solumuz görüntünün soluna, sağımız görüntünün sağına yerleşmiş olur
    if not ret :
        print("kameradan görüntü okunamıyor")
        break
    cv2.imshow("Video", frame)
    if cv2.waitKey(30) & 0xFF == ord('q') : ## 30milisaniye'de görüntü al ve çıkış eşit se q'a çık
        print("kamera kapatıldı")
        break
cam.release() # okumada olan kamerayı serbest bırak

cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar

