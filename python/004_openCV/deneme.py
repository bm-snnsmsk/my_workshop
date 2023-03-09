import cv2
import numpy as np
from random import randint


# image1 = np.zeros((200,200,3), np.uint8)
# image2 = np.zeros((200,200,3), np.uint8)
# for i in range(0,200) :
#     for j in range(0,200) :
#         image1[i, j] = [255,255,255]
# cv2.imshow("opencv", np.hstack([image1, image2]))
# cv2.imwrite("images/siyah_beyaz.png", np.hstack([image1, image2]))


image = np.zeros((300,300), np.uint8)
for i in range(20) :
    cv2.circle(image, (randint(0,300),randint(0,300)), randint(5,15), (255,255,255), -1)
cv2.imshow("opencv", image)
cv2.imwrite("images/beyaz_daire.png", image)


##-------------- zıtlaştırma START ------------------##
# 1. yol uzun yol
# resim = cv2.imread("images/avatar4.png")
# print(resim.shape)
# for i in range(225) :
#     for j in range(225) :
#         resim[i, j] = 255 - resim[i, j]
#         # print(f"{i} x {j} = {resim[i, j]} => {255 - resim[i, j]}")
# cv2.imshow("opencv", resim)

# 2. yolo kısa yol
# resim = cv2.imread("images/avatar4.png")
# bit_not = cv2.bitwise_not(resim)
# cv2.imshow("opencv", bit_not)
##-------------- zıtlaştırma END ------------------##

##------------------ arkaplanı yapıştırı1an fotonun arkaplanı yapma START ----------------------##

# img1 = cv2.imread("images/kadin.png")
# img2 = cv2.imread("images/3.jpg")

# img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img1_gray, 15, 255, cv2.THRESH_BINARY) 

# x,y,z = img1.shape 
# roi = img2[0:x, 0:y] 


# mask_inv = cv2.bitwise_not(mask)


# img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv) 
# img2_fg = cv2.bitwise_and(img1, img1, mask=mask)

# toplam = cv2.add(img1_bg, img2_fg)
# img2[0:x, 0:y] = toplam 


# cv2.namedWindow("img2", cv2.WINDOW_NORMAL)
# cv2.imshow("mask",mask)
# cv2.imshow("mask_inv",mask_inv)
# cv2.imshow("img1_bg",img1_bg)
# cv2.imshow("img2_fg",img2_fg)
# cv2.imshow("toplam",toplam)
# cv2.imshow("img2",img2)
##------------------ arkaplanı yapıştırılan fotonun arkaplanı yapma END ------------------------##

##------------------ zeros START ----------------------##
# resim = np.zeros((512,512,3),np.uint8) + 255 ## beyaz tuval
# print(resim)
# cv2.imshow("numpy", resim)  
##------------------ zeros END ------------------------##


cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar

