import cv2

## uygulama alanları
## göz kırpma, plaka tanımlama vb..

# resim = cv2.imread("images/gurultulu_3.jpg") ## numpy array'ine dönüştürme
resim = cv2.imread("images/gurultulu_4.png") ## numpy array'ine dönüştürme
# resim = cv2.imread("images/gurultulu_resim.jpg") ## numpy array'ine dönüştürme

##------------------------- gauss filtering START ---------------------------------------##
## Ele alınan matris şablonundaki tüm değerlerin çan eğrisi alınarak filtreleme yapılır.
# median_filter_1 = cv2.medianBlur(resim, 3) ## (img, sablon(3X3 mü 5X5 mi ..))
# gauss_filter_1 = cv2.GaussianBlur(resim, (7,9), 0) ## (img, sablon(3X3 mü 5X5 mi ..))
gauss_filter_2 = cv2.GaussianBlur(resim, (5,5), 0) ## (img, sablon(3X3 mü 5X5 mi ..))
# gauss_filter_3 = cv2.GaussianBlur(resim, (7,7), 0) ## (img, sablon(3X3 mü 5X5 mi ..))
##------------------------- gauss filtering END -----------------------------------------##
gauss_filter_5 = cv2.GaussianBlur(gauss_filter_2, (5,5), 0) ## (img, sablon(3X3 mü 5X5 mi ..)) = kernel, standart sapma
gauss_filter_6 = cv2.medianBlur(gauss_filter_5, 3) ## (img, sablon(3X3 mü 5X5 mi ..))


# cv2.imshow("OpenCV", resim)  ## belirtilen resmi gösterme
# cv2.imshow("3X3 median", median_filter_1)  ## belirtilen resmi gösterme
# cv2.imshow("3X3 gauss", gauss_filter_1)  ## belirtilen resmi gösterme
cv2.imshow("5X5 gauss", gauss_filter_2)  ## belirtilen resmi gösterme
cv2.imshow("5 ", gauss_filter_5)  ## belirtilen resmi gösterme
cv2.imshow("6 ", gauss_filter_6)  ## belirtilen resmi gösterme
# cv2.imshow("7X7 gauss", gauss_filter_3)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 