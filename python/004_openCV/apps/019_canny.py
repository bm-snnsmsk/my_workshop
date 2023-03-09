import cv2
import numpy as np

resim = cv2.imread("images/groot.png") ## numpy array'ine dönüştürme

## canny için gray foto olmalı
## varsa çizgileri kaldırmak için filtreleme yapılmalı
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)

canny = cv2.Canny(blur, 75, 225) ##img, alt_eşik, üst_eşik

def auto_canny(img, sigma = 0.33) :
    median = np.median(blur)
    lower = int(max(0, (1.0 - sigma) * median)) ## alt eşik değer
    upper = int(min(255, (1.0 + sigma) * median)) ## upper eşik değer
    canny = cv2.Canny(img, lower, upper) 
    return canny



# cv2.imshow("canny", canny)  ## belirtilen resmi gösterme
# cv2.imshow("canny auto", auto_canny(blur))  ## belirtilen resmi gösterme
cv2.imshow("tum pencereler", np.hstack([canny, auto_canny(blur)])) ## tüm örnekler tek pencerede


cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 