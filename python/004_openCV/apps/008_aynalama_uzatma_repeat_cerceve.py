import cv2

resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme

##---------------------------- aynalama START ------------------------------------------##
aynalananResim = cv2.copyMakeBorder(resim,215,215,215,215, cv2.BORDER_REFLECT) ## img,top,bot,left,right,property
##---------------------------- aynalama END --------------------------------------------##

##---------------------------- uzatma START ------------------------------------------##
uzatilanResim = cv2.copyMakeBorder(resim,75,75,150,150, cv2.BORDER_REPLICATE)## img,top,bot,left,right,property
##---------------------------- uzatma END --------------------------------------------##

##--------------------------- tekrarlanma START -----------------------------------------##
tekrarlananResim = cv2.copyMakeBorder(resim,430,430,430,430, cv2.BORDER_WRAP)  ## img,top,bot,left,right,property
##--------------------------- tekrarlanma END -------------------------------------------##

##--------------------------- çerçeveleme START -----------------------------------------##
cercevelenenResim = cv2.copyMakeBorder(resim,10,10,10,10, cv2.BORDER_CONSTANT,value=(175,150,15))## img,top,bot,left,right,property,frame_color(default_color=siyah)
##--------------------------- çerçeveleme END -------------------------------------------##

cv2.imshow("Aynalama", aynalananResim)  ## belirtilen resmi gösterme
cv2.imshow("Uzatma", uzatilanResim)  ## belirtilen resmi gösterme
cv2.imshow("Tekrarlanma", tekrarlananResim)  ## belirtilen resmi gösterme
cv2.imshow("Cerceveleme", cercevelenenResim)  ## belirtilen resmi gösterme

cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


 