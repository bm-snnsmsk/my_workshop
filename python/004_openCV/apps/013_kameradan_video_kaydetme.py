import cv2

cam = cv2.VideoCapture("images/pexels.mp4")


while cam.isOpened() :
    ret, frame = cam.read()  
    if not ret : ## kısa süreli videoda burası çalıştı
        print("kameradan görüntü okunamyır")
        break
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0XFF == ord('q') :
        print("Video kapatıldı")
        break

cam.release()
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 