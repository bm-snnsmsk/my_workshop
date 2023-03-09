import cv2
import numpy as np

## morfolojik işlemler gürültüleri azaltmak için kullanılırlar
## ayrıca morfolojik işlemler her zaman binary resimler üzerinde yapılır

resim = cv2.imread("images/beyaz_daire.png") ## numpy array'ine dönüştürme
kernel = np.ones((5,7), np.uint8) ## ne kadar büyük olsa aşınım o kadar büyük olur. ihtiyacımız kadar büyük olmalı, hep tek sayı olmalıdırlar
kernel2 = np.ones((15,17), np.uint8) ## ne kadar büyük olsa aşınım o kadar büyük olur. ihtiyacımız kadar büyük olmalı, hep tek sayı olmalıdırlar

erosion = cv2.erode(resim, kernel, iterations=5) ## görselde gürültü varsa, gürültü giderici, inceltme, aşındırma , iterasyon değeri erode'i daha da inceltir
dilation = cv2.dilate(erosion, kernel2, iterations = 5) ## sonra gürültü giderilmiş olan görsele dilation yapılır

cv2.imshow("orginal", resim)  ## belirtilen resmi gösterme
cv2.imshow("dilate", dilation)  ## belirtilen resmi gösterme
cv2.imshow("erode", erosion)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 