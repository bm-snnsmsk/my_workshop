import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/opencv.png")
blue = [255,0,0]
print(img.shape)
replicate = cv2.copyMakeBorder(img, 249,249,202,202,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 249,249,202,202,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 249,249,202,202,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 249,249,202,202,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 249,249,202,202,cv2.BORDER_CONSTANT, value=blue)

 ## birden fazla pencere gösterimi için (2 satır 3 sütün 1. hücre)
plt.subplot(231),plt.imshow(img,"gray"),plt.title("original")
## birden fazla pencere gösterimi için (2 satır 3 sütün 2. hücre)
plt.subplot(232),plt.imshow(replicate,"gray"),plt.title("replicate")
plt.subplot(233),plt.imshow(reflect,"gray"),plt.title("reflect")
plt.subplot(234),plt.imshow(reflect101,"gray"),plt.title("reflect101")
plt.subplot(235),plt.imshow(wrap,"gray"),plt.title("wrap")
plt.subplot(236),plt.imshow(constant,"gray"),plt.title("constant")
   
plt.show() 
    

