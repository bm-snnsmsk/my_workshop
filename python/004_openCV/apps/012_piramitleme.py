import cv2

resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme

iki_kat_buyuk = cv2.pyrUp(resim) ## orjinal resmin iki kat büyüğü
iki_kat_kucuk = cv2.pyrDown(resim)  ## orjinal resmin iki kat küçüğü

print(resim.shape)
print(iki_kat_buyuk.shape)
print(iki_kat_kucuk.shape)

cv2.imshow("OpenCV", resim)  ## belirtilen resmi gösterme
cv2.imshow("iki kat Buyutulmus Resim", iki_kat_buyuk)  ## belirtilen resmi gösterme
cv2.imshow("iki kat kucutulmus Resim", iki_kat_kucuk)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 