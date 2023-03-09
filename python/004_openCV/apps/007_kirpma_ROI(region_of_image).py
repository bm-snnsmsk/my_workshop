import cv2
import matplotlib.pyplot as plt

## amaç işlemleri hızlandırmak için
## örneğin göz taranacaksa yüz tespiti yapılmış bir alanda göz aramak işlemi daha da hızlandıracaktır
img = cv2.imread("images/avatar4.png")

# img[:,:, 0] = 0 ## resimdeki tüm blue kanalı sıfırlamak
# img[:,:, 1] = 0 ## resimdeki tüm green kanalı sıfırlamak
# img[:,:, 2] = 0 ## resimdeki tüm red kanalı sıfırlamak

kirp = img[90:120, 55:170]
img[10:40, 55:170] = kirp
plt.subplot(121) ## birden fazla pencere gösterimi için (1 satır 2 sütün 1. hücre)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))   
plt.subplot(122) ## birden fazla pencere gösterimi için (1 satır 2 sütün 2. hücre)
plt.imshow(cv2.cvtColor(kirp, cv2.COLOR_BGR2RGB))   
plt.title("yeni baslik") ## baslik atama
plt.xticks([]) ## x grafiğini kaldır
plt.yticks([]) ## y grafiğini kaldır
plt.show() 
    

