import cv2
import numpy as np

resim = cv2.imread("images/gurultulu_3.jpg",0) ## numpy array'ine dönüştürme

## thresh için imread(img, 0 ) olmak zorunda
thres1 = cv2.adaptiveThreshold(resim, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 23,6) 
thres2 = cv2.adaptiveThreshold(resim, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 23,6) 

cv2.imshow("orginal", resim)  ## belirtilen resmi gösterme
cv2.imshow("threshold mean", thres1)  ## belirtilen resmi gösterme
cv2.imshow("threshold gauss", thres2)  ## belirtilen resmi gösterme


cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 