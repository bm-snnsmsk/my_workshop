import cv2


## ROI
resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme
kesit = resim[75:125,20:200] ## y0:y1;, x0:x1

cv2.imshow("Kesit", kesit)  ## belirtilen resmi gösterme
cv2.imshow("OpenCV", resim)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


