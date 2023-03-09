import cv2
import numpy as np

## bitsel çarpma
##   010111001
##   011101011
## X__________
##   010101001 


img = cv2.imread("images/OpenCV.jpg")
img2 = cv2.imread("images/3.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY) ## 10 altındakiler siyah üstündekiler ise 255(beyaz)
## bu işlemlerde amaç arkadaki belirlenen tonu siyah yani 0 yap
# üzerinde çalışılan img ile bitsel çarpma işlemi yap
# belirlenen değerin altındakiler 0 olacağı için ve bu 0'lar her ne ile çarpılacaksa 0 sonuç verir
# geri kalan kısımlar ise 1 ile çarpılacağından kendi renklerini verir ve işlem istenen şekilde maskelenmiş olur....  

cv2.imshow("resim",img_gray)
cv2.imshow("resim2",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()