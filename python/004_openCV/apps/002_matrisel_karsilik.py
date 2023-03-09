import cv2

resim = cv2.imread("images/icon.png") ## numpy array'ine dönüştürme (RGB) varsayılan
resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme, 0 = Siyah- Beyaz ton Farkı daha hızlı işlem yapar

cv2.imshow("Pencere Adı (sol-ust kosede) (türkçe karakterleri okumuyor)", resim)  ## belirtilen resmi gösterme
print(resim) ## matrisel karşılığı verir

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


