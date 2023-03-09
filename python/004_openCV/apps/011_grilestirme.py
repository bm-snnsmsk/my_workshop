import cv2

resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme

resim_gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY) ## = cv2.imread("images/avatar4.png", 0)

yukseklik, genislik, kanal = resim.shape
print("Original : ",yukseklik, genislik, kanal)
print("Gri Ton  : ",resim_gri.shape)

cv2.imshow("OpenCV", resim)  ## belirtilen resmi gösterme
cv2.imshow("Gri Resim", resim_gri)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 