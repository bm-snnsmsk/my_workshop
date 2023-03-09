import cv2
import numpy as np

resim = cv2.imread("images/avatar4.png",0) ## numpy array'ine dönüştürme

## thresh için imread(img, 0 ) olmak zorunda
## tüm piksellere bu işlem uygulanır
ret, thres1 = cv2.threshold(resim, 127, 255, cv2.THRESH_BINARY) ## img, eşik_değer(eşikdeğer altındakiler = 0 olacak), (eşik değer yukarısındakileri ise biz belirliyoruz), thres flagı(type'i) (simple thresh) 
ret, thres2 = cv2.threshold(resim, 127, 255, cv2.THRESH_BINARY_INV) ## img, eşik_değer(eşikdeğer altındakiler = 0 olacak), (eşik değer yukarısındakileri ise biz belirliyoruz), thres flagı(type'i) (thresh inv) thresh1'in tam tersi
ret, thres3 = cv2.threshold(resim, 127, 255, cv2.THRESH_TRUNC) ## img, eşik_değer(eşikdeğer altındakiler = 0 olacak), (eşik değer yukarısındakileri ise biz belirliyoruz), thres flagı(type'i) (thresh trunc) thresh1'in tam tersi
ret, thres4 = cv2.threshold(resim, 127, 255, cv2.THRESH_TOZERO) ## img, eşik_değer(eşikdeğer altındakiler = 0 olacak), (eşik değer yukarısındakileri ise biz belirliyoruz), thres flagı(type'i) (thresh tozero) thresh1'in tam tersi
ret, thres5 = cv2.threshold(resim, 127, 255, cv2.THRESH_TOZERO_INV) ## img, eşik_değer(eşikdeğer altındakiler = 0 olacak), (eşik değer yukarısındakileri ise biz belirliyoruz), thres flagı(type'i) (thresh tozero_inv) thresh1'in tam tersi
cv2.imshow("orginal", resim)  ## belirtilen resmi gösterme
cv2.imshow("threshold 1", thres1)  ## belirtilen resmi gösterme
cv2.imshow("threshold 2", thres2)  ## belirtilen resmi gösterme
cv2.imshow("threshold 3", thres3)  ## belirtilen resmi gösterme
cv2.imshow("threshold 4", thres4)  ## belirtilen resmi gösterme
cv2.imshow("threshold 5", thres5)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 