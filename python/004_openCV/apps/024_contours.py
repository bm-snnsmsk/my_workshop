import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/sekiller.png")
img = cv2.imread("images/groot.png")
img = cv2.imread("images/contours.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray_img, 50, 100) ## değerler şimdilik deneme yanılma yoluyla ama mantıklısıya tracbar yada GUI aracı slider
contours, hierarcy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("counters sayısı : ",str(len(contours)))
cv2.drawContours(img, contours, -1, (255, 0, 0), 1) ## tüm kontorları çiz veya belli bir contours[0] ilk contoru çiz











print(img.shape)
print(gray_img.shape)



cv2.imshow("contours", edged)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


 