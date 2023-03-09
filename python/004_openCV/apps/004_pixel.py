import cv2

resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme

cv2.imshow("Pencere Adı (sol-ust kosede) (türkçe karakterleri okumuyor)", resim)  ## belirtilen resmi gösterme

# print(resim)  ## tüm matrisler
print(resim[(200,80)])  ## belirtilen y, x noktasındaki  BGR değeri =  [105 161 221]
print(resim[(200,80, 0)])  ## belirtilen y, x noktasındaki  B değeri =  105
print(resim[(200,80, 1)])  ## belirtilen y, x noktasındaki  G değeri =  161
print(resim[(200,80, 2)])  ## belirtilen y, x noktasındaki  R değeri =  221

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


