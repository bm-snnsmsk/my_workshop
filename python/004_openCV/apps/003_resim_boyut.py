import cv2

resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme

cv2.imshow("Pencere Adı (sol-ust kosede) (türkçe karakterleri okumuyor)", resim)  ## belirtilen resmi gösterme

print(resim.size) ## resmin boyutunu verir => genişlik X yükseklik X kanal = resim.size
print(resim.dtype) ## data tipini verir  uint8 == 8 bitlik
print(resim.shape) ## genişlik - yükseklik - kanal sayısı => (215, 215, 3) siyah beyaz olsaydı => (215, 215) kanal sayısı 1 olduğu için yazılmamış  => genişlik X yükseklik X kanal = resim.size

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


