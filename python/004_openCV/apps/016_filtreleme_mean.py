import cv2

## gürültü azaltma veya blurlaştırma 

# resim = cv2.imread("images/gurultulu_3.jpg") ## numpy array'ine dönüştürme
resim = cv2.imread("images/gurultulu_4.png") ## numpy array'ine dönüştürme
# resim = cv2.imread("images/gurultulu_resim.jpg") ## numpy array'ine dönüştürme

##------------------------- mean filtering START ---------------------------------------##
## Ele alınan matris şablonundaki tüm değerlerin ortalamasını alınarak yeni bir image oluşturmya dayalı bir yumuşatma işlemi, bir filtrelemedir
## örneğin 3x3 = 9 matrisin ortalaması alınır ve ortadaki matrise yazılır
mean_filter_1 = cv2.blur(resim, (3,3)) ## (img, sablon(3X3 mü 5X5 mi ..)) = kernel
mean_filter_2 = cv2.blur(resim, (5,5)) ## (img, sablon(3X3 mü 5X5 mi ..))  = kernel
mean_filter_3 = cv2.blur(resim, (15,15)) ## (img, sablon(3X3 mü 5X5 mi ..))  = kernel
##------------------------- mean filtering END -----------------------------------------##


cv2.imshow("OpenCV", resim)  ## belirtilen resmi gösterme
cv2.imshow("3X3 Filtreleme", mean_filter_1)  ## belirtilen resmi gösterme
cv2.imshow("5X5 Filtreleme", mean_filter_2)  ## belirtilen resmi gösterme
cv2.imshow("15X15 Filtreleme", mean_filter_3)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 