import cv2
import numpy as np


## cv2 içindeki COLOR_ ile başlayan fonksiyonlar 
for i in dir(cv2) :
    if 'COLOR_' in i :
        print(i)
## renk tespitlerinde HSV renk uzayı daha avantajlıdır

def nothing(x) :
    pass
cv2.namedWindow("Frame")
cv2.createTrackbar("H1", "Frame", 0, 359, nothing)
cv2.createTrackbar("H2", "Frame", 0, 359, nothing)
cv2.createTrackbar("S1", "Frame", 0, 255, nothing)
cv2.createTrackbar("S2", "Frame", 0, 255, nothing)
cv2.createTrackbar("V1", "Frame", 0, 255, nothing)
cv2.createTrackbar("V2", "Frame", 0, 255, nothing)

cam = cv2.VideoCapture(0)
cam.set(3, 250)
cam.set(4, 250)



# yesil = np.uint8([[[0,255,0]]])
# hsv_yesil = cv2.cvtColor(yesil, cv2.COLOR_BGR2HSV)
# print(hsv_yesil)

while cam.isOpened() :
    _, frame = cam.read() 
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    H1 = int(cv2.getTrackbarPos("H1", "Frame") ) ## / 2 silinince daha düzgün sonuçlar vermeye başladı
    H2 = int(cv2.getTrackbarPos("H2", "Frame") ) ## / 2 silinince daha düzgün sonuçlar vermeye başladı
    S1 = cv2.getTrackbarPos("S1", "Frame")
    S2 = cv2.getTrackbarPos("S2", "Frame")
    V1 = cv2.getTrackbarPos("V1", "Frame")
    V2 = cv2.getTrackbarPos("V2", "Frame")

    ## normalde HSV renk uzayında H değeri 360 iken cv2 'de 180 derece. 180 dereceden sonra tekrar başa geçer
    lower = np.array([H1,S1,V1]) ## h, s, v     h(110 - 130) = blue  h(50 - 70) = blue 
    upper = np.array([H2,S2,V2]) ## h, s, v   h(110 - 130) = blue  h(50 - 70) = blue
    color_mask = cv2.inRange(hsv, lower, upper)

    result = cv2.bitwise_and(frame, frame, mask=color_mask)

    cv2.imshow("Frame", frame)
    # cv2.imshow("hsv", hsv)
    cv2.imshow("mask", color_mask)
    cv2.imshow("result", result)

    if cv2.waitKey(1) == ord('q') :
        break

cam.release()
cv2.destroyAllWindows()
