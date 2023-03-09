import cv2

resim = cv2.imread("images/gurultulu_3.jpg") ## numpy array'ine dönüştürme
# resim = cv2.imread("images/gurultulu_4.png") ## numpy array'ine dönüştürme
# resim = cv2.imread("images/gurultulu_resim.jpg") ## numpy array'ine dönüştürme

##------------------------- median filtering START ---------------------------------------##
## Ele alınan matris şablonundaki tüm değerler küçükten büyüğe sıralanır ordaki değer orta matrise yazılırak filtreleme yapılır.
median_filter_1 = cv2.medianBlur(resim, 3) ## (img, sablon(3X3 mü 5X5 mi ..))
median_filter_2 = cv2.medianBlur(resim, 5) ## (img, sablon(3X3 mü 5X5 mi ..))
median_filter_3 = cv2.medianBlur(resim, 15) ## (img, sablon(3X3 mü 5X5 mi ..))
##------------------------- median filtering END -----------------------------------------##


# cv2.imshow("OpenCV", resim)  ## belirtilen resmi gösterme
cv2.imshow("3X3 median", median_filter_1)  ## belirtilen resmi gösterme
cv2.imshow("5X5 median", median_filter_2)  ## belirtilen resmi gösterme
cv2.imshow("15X15 median", median_filter_3)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 