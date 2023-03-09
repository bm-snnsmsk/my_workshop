import cv2

resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme

# resim[:,:,0] = 255 ## blue efekti
# resim[:,:,1] = 255 ## green efekti
# resim[:,:,2] = 255 ## red efekti

## ikisinin karışımı yellow efekti
# resim[:,:,1] = 255 ## green efekti
# resim[:,:,2] = 255 ## red efekti
## ikisinin karışımı yellow efekti

## blue ve green karışımı efekti
# resim[:,:,0] = 125 ## blue efekti
# resim[:,:,1] = 125 ## green efekti
##  blue ve green karışımı efekti

## blue, green ve red karışımı efekti  3 renk kullanımında renklerin karışımı olan efekt remi baskılıyor
# resim[:,:,0] = 255 ## blue efekti
# resim[:,:,1] = 0 ## green efekti
# resim[:,:,2] = 255 ## red efekti
##  blue, green ve red karışımı efekti 3 renk kullanımında renklerin karışımı olan efekt remi baskılıyor

## belli bir bölgeye efekt uygulama
resim[75:125,20:200,0] = 255 ##  y0:y1, x0:x1, renk
resim[75:125,20:200,1] = 255 ##  y0:y1, x0:x1, renk
##  belli bir bölgeye efekt uygulama




cv2.imshow("OpenCV", resim)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


