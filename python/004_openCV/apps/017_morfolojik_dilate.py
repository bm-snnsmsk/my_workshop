import cv2
import numpy as np

## morfolojik işlemler gürültüleri azaltmak için kullanılırlar
## ayrıca morfolojik işlemler her zaman binary resimler üzerinde yapılır

resim = cv2.imread("images/beyaz_daire.png") ## numpy array'ine dönüştürme
kernel = np.ones((15,7), np.uint8)
dilation = cv2.dilate(resim, kernel,iterations = 1) ## ( , , iterations) ## beyaz bölge artmış olur, bir nevi sayfaya gürültü eklenmiş olur, görselde kesikler varsa dilate kullamak daha mantıklıdır, kalınlaştırma
dilation2 = cv2.dilate(resim, kernel, 22) ## ( , , iterations) ## beyaz bölge artmış olur, bir nevi sayfaya gürültü eklenmiş olur, görselde kesikler varsa dilate kullamak daha mantıklıdır, kalınlaştırma iterasyon değeri dilate'i daha da kalınlaştırır

cv2.imshow("original", resim)  ## belirtilen resmi gösterme
cv2.imshow("OpenCV", dilation)  ## belirtilen resmi gösterme
cv2.imshow("OpenCV2", dilation2)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 