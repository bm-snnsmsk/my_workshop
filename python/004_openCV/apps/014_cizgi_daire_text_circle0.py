import cv2
import numpy as np


resim = np.ones((512,512,3),np.uint8)  ## h - w
print(resim)

cv2.line(resim, (0,0), (511,511), (255,0,255), 2)
cv2.line(resim, (200,10), (10,200), (0,0,255), 2)

cv2.rectangle(resim, (110,110), (400,400), (0,255,255), 2)
cv2.rectangle(resim, (200,404), (312,511), (0,255,255), -1) ## -1 içi dolu

cv2.circle(resim, (200,200), 50, (125,125,0), 2)
cv2.circle(resim, (300,300), 50, (0,125,125), -1)

cv2.ellipse(resim, (135,350), (30,50),0,0,360, (125,0,125), 2)
cv2.ellipse(resim, (335,150), (30,50),0,0,360, (125,0,255), -1)

pts = np.array([[400,20], [430,15], [470,120], [450,90], [410,50]], np.int32)
pts2 = np.array([[10,320], [20,315], [70,320], [100,390], [110,450]], np.int32)
pts.reshape(-1,1,2)
cv2.polylines(resim, [pts], True, (120,254,200), 2) ## Treu olursa ilk ve on nokta birleştirlir, False olursa ilk ve son nokta birleştirilmez
cv2.polylines(resim, [pts2], False, (120,254,200), 2) ## Treu olursa ilk ve on nokta birleştirlir, False olursa ilk ve son nokta birleştirilmez

cv2.putText(resim,"Sinan", (256,256), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 1, cv2.LINE_AA)



cv2.imshow("numpy sekiller", resim)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 