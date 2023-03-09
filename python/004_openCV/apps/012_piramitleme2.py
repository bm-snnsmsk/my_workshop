import cv2
import numpy as np

resim = np.zeros((225,225,3), dtype="uint8") ## (shape, datatype) => tüm elemanları 0 olan matris oluşturur
resim2 = np.ones([225,225,3]) ## (shape, datatype) => tüm elemanları 1 olan matris oluşturur
# resim2 = np.ones((225,225,3)) ## (shape, datatype) => tüm elemanları 1 olan matris oluşturur
print(resim2) ## 1. şeklinde çıkıyor !!! çünkü float fakat uint8 yazınca da siyah bir görsel çıkıyor !!!

cv2.namedWindow("siyah",cv2.WINDOW_NORMAL) ## mouse ile resize edilir bir pencere olur
cv2.namedWindow("beyaz",cv2.WINDOW_NORMAL) ## mouse ile resize edilir bir pencere olur

cv2.imshow("siyah", resim) ## tüm pikseller 0 olduğundan siyah bir resim çıkar
cv2.imshow("beyaz", resim2) ## tüm pikseller 1 olduğundan beyaz bir resim çıkar 

cv2.waitKey(0)
cv2.destroyAllWindows()
 