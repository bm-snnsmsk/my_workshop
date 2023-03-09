import cv2

resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme

kirpma = cv2.rectangle(resim, (20,200), (200,10), [0,0,255], 3) ## img, sol-alt(x,y), sağ-üst(x,y), BGR, kenarlık(0,9 arası)

cv2.imshow("OpenCV", resim)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 