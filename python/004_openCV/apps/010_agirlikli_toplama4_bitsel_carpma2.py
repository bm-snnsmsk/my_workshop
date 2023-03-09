import cv2
import numpy as np

### DİKKAT arkplan siyah olan görselde tam çalışıyor 

## bitsel çarpma
##   010111001
##   011101011
## X__________
##   010101001 

## bu işlemlerde amaç arkadaki belirlenen tonu siyah yani 0 yap
# üzerinde çalışılan img ile bitsel çarpma işlemi yap
# belirlenen değerin altındakiler 0 olacağı için ve bu 0'lar her ne ile çarpılacaksa 0 sonuç verir
# geri kalan kısımlar ise 1 ile çarpılacağından kendi renklerini verir ve işlem istenen şekilde maskelenmiş olur....  

img1 = cv2.imread("images/avatar4.png")
img2 = cv2.imread("images/3.jpg")

x,y,z = img1.shape ## 3 değer dödürür (height, weight, kanal)
roi = img2[0:x, 0:y] ## 2. resimden 1. resim boyutunda kırpma yapıldı

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img1_gray, 10, 255, cv2.THRESH_BINARY) 

mask_inv = cv2.bitwise_not(mask) ## tersleme işlemi // amaç bu fotonun arkaplanı 0 yapılıp ana img'ın görüntüsü ortaya çıksın diye


img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv) ## neden roi, roi cünkü yukarda anlatıldığı gibi bitsel çarpma yapılsa 
## örneğin
# 001011      - 11
# 000101      -  5
# -------     - 
# 000001      -  1     (11 * 5 != 1) 
# işte bu yanlış işelm olöasın diye sadece maskeleme işlemi olsun diye böyle bir şey denemiş 
img2_fg = cv2.bitwise_and(img1, img1, mask=mask)

## bu son işlemn ile arka plan 2. görselden alınarak esas image eklenmiş olur
toplam = cv2.add(img1_bg, img2_fg)
img2[0:x, 0:y] = toplam ## bu işlem ile de arka planı değiştirilmiş resim büyük image'e, küçük image boyutunda yerleştirilmiş olur

cv2.namedWindow("resim", cv2.WINDOW_NORMAL)
cv2.imshow("resim",img2)
cv2.imshow("resim2",toplam)

cv2.waitKey(0)
cv2.destroyAllWindows()