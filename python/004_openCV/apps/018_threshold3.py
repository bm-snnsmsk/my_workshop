import cv2
import numpy as np

resim = cv2.imread("images/gurultulu_3.jpg",0) ## numpy array'ine dönüştürme

## thresh için imread(img, 0 ) olmak zorunda
ret, thres1 = cv2.threshold(resim, 0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) ## min max ( min-max araında otomatik olarak bir eşik değer alır)eşik değeri

cv2.imshow("orginal", resim)  ## belirtilen resmi gösterme
cv2.imshow("threshold mean", thres1)  ## belirtilen resmi gösterme


cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 