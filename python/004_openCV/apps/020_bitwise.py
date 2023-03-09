import cv2
import numpy as np

resim1 = cv2.imread("images/siyah_beyaz.png") ## numpy array'ine dönüştürme
resim2 = cv2.imread("images/beyaz_daire.png") ## numpy array'ine dönüştürme



bit_and = cv2.bitwise_and(resim1, resim2) ## tüm pikselleri toplar 1 and 1 = 1 (1 beyaz, 0 siyah)
bit_or = cv2.bitwise_or(resim1, resim2) ## 1 or 0 = 1 (1 beyaz, 0 siyah)
bit_xor = cv2.bitwise_xor(resim1, resim2) ## 1 xor 1 = 0, 0 xor 0 = 0, 0 xor 1 = 1, 0 xor 1 = 1  (1 beyaz, 0 siyah)
bit_not = cv2.bitwise_not(resim2) ## not 1 = 0, not 0 = 1

cv2.imshow("resim1", resim1) 
cv2.imshow("resim2", resim2) 
cv2.imshow("bitwise and", bit_and) 
cv2.imshow("bitwise or", bit_or) 
cv2.imshow("bitwise xor", bit_xor) 
cv2.imshow("bitwise not", bit_not) 
# cv2.imshow("tum pencereler", np.hstack([resim1, resim2])) 


cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 