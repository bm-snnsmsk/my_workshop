import cv2
import numpy as np


##------------------ zeros START ----------------------##
resim = np.zeros((512,512,3),np.uint8) + 255 ## beyaz tuval
print(resim)
cv2.line(resim, (0,0), (511,511), (255,0,0), 2)
cv2.rectangle(resim, (50,50), (300,300), (0,0,255), 2)
cv2.circle(resim, (450,450), (50), (0,255,0), -1)
cv2.imshow("numpy", resim)  
##------------------ zeros END ------------------------##


cv2.waitKey(0) 
cv2.destroyAllWindows() 

