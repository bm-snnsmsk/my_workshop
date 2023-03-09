import cv2

## her piksel(nokta) bir matristir
## her matris OpenCV'de BGR olarak, renk kodlarının karşılığı olan bir rakamla ifade edilir
## dolayısıyla bir piksele max 255, min 0 değerleri verilebilir

# resim = cv2.imread("3.jpg") ## numpy array'ine dönüştürme  
# resim = cv2.imread("avatar4.png") ## numpy array'ine dönüştürme
resim = cv2.imread("images/icon.png") ## numpy array'ine dönüştürme (RGB) varsayılan
resim = cv2.imread("images/icon.png", 0) ## numpy array'ine dönüştürme, 0 = Siyah- Beyaz ton Farkı daha hızlı işlem yapar, bellek ve hız açısından avantaj sağlar

resim = cv2.imread("images/avatar4.png")
print(resim) ## tüm piksel renkler,
cv2.imshow("Pencere Adı (sol-ust kosede) (türkçe karakterleri okumuyor)", resim)  ## belirtilen resmi gösterme
cv2.imwrite("images/yeni_icon_resmi.png", resim) ## istenirse şayet bu kodla renkleri sıfırlanan yeni resim yeni isimle kaydedilebilir veya aynı isimle varolan resim yenisiyle değiştirilmiş olur

key = cv2.waitKey(0) ## pencere açıldığında ekranda durup görmemiz için, 0 = klavyeden herhangi bir tuşa basana kadar bekler veya ekranda kalacak süreyi milisaniye cinsinden belirtebiliriz, key = basılan tuşun değeri
print(key)
cv2.destroyAllWindows() ## herhangi bir tuşa basıldığında OpenCV'e ait tüm pencerenin kapanmasını sağlar


