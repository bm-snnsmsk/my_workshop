import cv2
from matplotlib import pyplot as plt


resim = cv2.imread("images/avatar4.png")

resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
resim = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)
resim = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)






print(resim) ## tüm piksel renkler,

cv2.namedWindow("resim",cv2.WINDOW_AUTOSIZE) ## pencere hazırlanır, hangi pencere içine konulkacaksa pencere isimleri aynı olmalı, pencere resize edilemez
cv2.namedWindow("resim",cv2.WINDOW_NORMAL) ## pencere resize edilebilir
cv2.imshow("resim", resim) 

# plt.imshow(resim) ## görüntüler opencv"de BGR matplotlib de ise RGB olarak okunur bu yüzden görüntülenme tam tersi olacaktır
plt.imshow(resim, cmap="gray") ## resim gray tonda olursa bu matplot da bu kodla gray olacaktır
plt.show()

key = cv2.waitKey(0) 
print(key)
if key == 27 : 
    print("esc tuşuna basıldı")
elif key == ord("q"):
    print("q tuşuna basıldı")
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


