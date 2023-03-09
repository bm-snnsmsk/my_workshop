import cv2
import numpy as np

# print(dir(cv2)) ## cv2 fonksiyonları
# for i in dir(cv2) :
#     if 'EVENT' in i :
#         print(i) ## mouse eventler

isDraw = False
mod = False
xi, yi = -1, -1
def mouse_events(event, x, y, flags, param) :
    # print(x,y)
    ##----------------- çift tıklanınca daire çiz START -------------------------------##
    # if event == cv2.EVENT_LBUTTONDBLCLK :
    #     print(x,y)
    #     cv2.circle(img, (x,y), 50, (255,0,0), -1)
    ##----------------- çift tıklanınca daire çiz END ---------------------------------##

    ##------------------ çizim işlemi START ----------------------##
    global isDraw, xi, yi, mod
    if event == cv2.EVENT_LBUTTONDOWN :
        xi, yi = x, y
        isDraw = True
    elif event == cv2.EVENT_MOUSEMOVE :
        if isDraw == True :
            if mod == True :
                cv2.circle(img, (x,y), 1, (100,50,0), -1)
            else :
                cv2.rectangle(img, (xi, yi), (x,y), (0,255,0), -1)
    elif event == cv2.EVENT_LBUTTONUP :
        isDraw == False
        if mod == True :
            cv2.circle(img, (xi,yi), 10, (100,50,0), -1)
        else :
            cv2.rectangle(img, (xi, yi), (x,y), (0,255,0), -1)
    ##------------------ çizim işlemi END ------------------------##

img = np.ones((512, 512, 3), np.uint8)

cv2.namedWindow("point")
cv2.setMouseCallback("point", mouse_events) ## hazır fonksiyon pencere isimleri aynı olmalı

while True :
    cv2.imshow("point", img)
    # if cv2.waitKey(0) : ## bu şekilde çalışmaz
    if cv2.waitKey(1) & 0xFF == ord('q') : # her bir saniyede kontrol et ve q'a basılmadığı sürece pencereyi ekranda tut
        break
    if cv2.waitKey(1) & 0xFF == ord('m') : # her bir saniyede kontrol et ve q'a basılmadığı sürece pencereyi ekranda tut
        mod = not mod


cv2.destroyAllWindows()


 