import cv2

resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme
resim2 = cv2.imread("images/icon.png") ## numpy array'ine dönüştürme

## üst üste bindirme olayında dikkat edilmei gereken şey iki görselin de boyutlarının aynı olması
res1 = resim[100,100]
res2 = resim2[100,100]
print(res1)
print(res2)

print(res1 + res2) ## toplam - 256
print(cv2.add(res1, res2)) ## toplam >= 255 = 255

toplam = cv2.add(resim, resim2) ## eşit oranda toplama
agirlikli_toplam = cv2.addWeighted(resim, 0.7, resim2, 0.3, 0) ## ağırlıklı oranda toplama, (0.0-1 aralığında oranlar verilmeli ve oranları  toplamı 1 olmalı), son parametre her zaman 0 olmalıymış
bit_top = cv2.bitwise_and(resim, resim2)

cv2.imshow("Avatar", resim)  ## belirtilen resmi gösterme
cv2.imshow("icon", resim2)  ## belirtilen resmi gösterme
cv2.imshow("toplanmis resim", toplam)  ## belirtilen resmi gösterme
cv2.imshow("agirlikli toplanmis resim", agirlikli_toplam)  ## belirtilen resmi gösterme
cv2.imshow("bit top", bit_top) 

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 