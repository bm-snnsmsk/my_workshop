import cv2
import numpy as np


resim = np.zeros((300,400,3), dtype="uint8") ## h - w
cv2.line(resim, (0,0), (20,100), (0,0,255), 3) ## img, (start_point(x,y)), (finish_point(x,y)), (color_BGR), kalınlık 
cv2.circle(resim, (50,150), 50, (0,255,0), 1) ## img, (center_point(x,y)), (radius), (color_BGR), kalınlık 
cv2.putText(resim, "Sinan Simsek - OpenCV Text Deneme", (0, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 2) ## img, text, text_center_point(x,y), font, font_size, color_BGR, kalınlık

cv2.imshow("numpy_resim", resim)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 