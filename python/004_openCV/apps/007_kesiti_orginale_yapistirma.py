import cv2

resim = cv2.imread("images/avatar4.png") ## numpy array'ine dönüştürme
kesit = resim[75:125,20:200] ## y0:y1;, x0:x1

resim[0:50,0:180] = kesit ## y'ler ve x'ler karşılıklı olarak aynı ölçüde olmalıdırlar
resim[0:50,0:180, 2] = 255 ## kesit bölümüne veya tamamına efect vermek istersek
resim[175:215,45:215, 1] = 255 ## belirlenen alana green efekti
resim[75:115,30:185] = (0,150,255)  ## belirlenen efekte (b,g,r) renk karışımını aktarma
cv2.imshow("OpenCV", resim)  ## belirtilen resmi gösterme



cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


