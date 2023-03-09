import cv2

resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme
resim2 = cv2.imread("images/icon.png") ## numpy array'ine dönüştürme

print(resim[100,200])
print(resim2[150,200])
print(resim[100,200]+resim2[150,200]) ## [ (B1+B2)%256, (G1+G2)%256, (R1+R2)%256 ]


cv2.imshow("Avatar", resim)  ## belirtilen resmi gösterme
cv2.imshow("icon", resim2)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 