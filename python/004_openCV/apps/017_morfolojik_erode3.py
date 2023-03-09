import cv2
import numpy as np

## morfolojik işlemler gürültüleri azaltmak için kullanılırlar
## ayrıca morfolojik işlemler her zaman binary resimler üzerinde yapılır

resim = cv2.imread("images/logom.png") ## numpy array'ine dönüştürme
kernel = np.ones((5,5), np.uint8)

closing = cv2.morphologyEx(resim,cv2.MORPH_CLOSE, kernel) ## dairelerin içindeki gürültüleri yok etmek için

cv2.imshow("orginal", resim)  ## belirtilen resmi gösterme
cv2.imshow("open", closing)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 