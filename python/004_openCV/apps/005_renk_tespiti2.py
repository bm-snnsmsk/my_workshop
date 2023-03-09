import cv2
import numpy as np


cam = cv2.VideoCapture(0)
cam.set(3, 250)
cam.set(4, 250)


while True :
    _, frame = cam.read() 
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ## green color detector START
    lower_green = np.array([45, 100, 50])
    upper_green = np.array([75, 255, 255]) ## ışık nesneye çok geliyorsa value değeri çok yüksek tutulabilir
    green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    ## green color detector END

    ## blue color detector START
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    ## blue color detector END


    cv2.imshow("webcam", frame)
    # cv2.imshow("green_mask", green_mask) ## bu gördüğü yeşil renkleri beyaz olarak gösterir diğer tüm renkler siyah olur
    # cv2.imshow("green", green) ## bu gördüğü yeşil renkleri yeşil olarak gösterir diğer tüm renkler siyah olur
    cv2.imshow("blue_mask", blue_mask) ## bu gördüğü blue renkleri beyaz olarak gösterir diğer tüm renkler siyah olur
    cv2.imshow("blue", blue) ## bu gördüğü blue renkleri blue olarak gösterir diğer tüm renkler siyah olur
    if cv2.waitKey(1) == ord('q') :
        break

cam.release()
cv2.destroyAllWindows()
