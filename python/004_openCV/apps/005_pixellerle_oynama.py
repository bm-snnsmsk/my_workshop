import cv2


## cv2 içindeki COLOR_ ile başlayan fonksiyonlar 
for i in dir(cv2) :
    if 'COLOR_' in i :
        print(i)



resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme


print(resim[(10,150)])  ## belirtilen y, x noktasındaki  BGR değeri =  [66 66 66]
print(resim[(10,150, 0)])  ## belirtilen y, x noktasındaki  B değeri =  66
print(resim[(10,150, 1)])  ## belirtilen y, x noktasındaki  G değeri =  66
print(resim[(10,150, 2)])  ## belirtilen y, x noktasındaki  R değeri =  66

## pixel pixel değiştirme
resim[0,150] = [255,0,0]  ## OpenCV BGR mantığıyla çalıştığı için RED değil blue bir çizgi çizer
resim[1,150] = [255,0,0]
resim[2,150] = [255,0,0]
resim[3,150] = [255,0,0]
resim[4,150] = [255,0,0]
resim[5,150] = [255,0,0]
resim[6,150] = [255,0,0]
resim[7,150] = [255,0,0]
resim[8,150] = [255,0,0]
resim[9,150] = [255,0,0]
resim[10,150] = [255,0,0]
resim[11,150] = [255,0,0]
resim[12,150] = [255,0,0]
resim[13,150] = [255,0,0]
resim[14,150] = [255,0,0]
resim[15,150] = [255,0,0]
resim[16,150] = [255,0,0]
resim[17,150] = [255,0,0]
resim[18,150] = [255,0,0]
resim[19,150] = [255,0,0]
resim[20,150] = [255,0,0]

## veya tabi yukardaki daha kulllanışlı
resim[157,112, 0] = 0
resim[157,112, 1] = 0
resim[157,112, 2] = 225

## veya
resim.itemset((157, 117, 0), 0)
print(resim[157, 117])
print(resim[157, 117, 0])
print(resim.item(157, 117, 0))

## veya tüm kanallar aynı renk olacaksa 
resim[157,115] = 0

##---------------- çizgi halinde pixellerle oynama START ------------------------------##
for i in range(215) :
    resim[i,50] = [0,0,255]  ## OpenCV BGR mantığıyla çalıştığı için BLUE değil RED bir çizgi çizer
##---------------- çizgi halinde pixellerle oynama END --------------------------------##


cv2.imshow("OpenCV", resim)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


