import cv2
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

print(x+y) ## 250 + 10 = 260 => 260 - 256 = 4 (8bit)
print(cv2.add(x, y)) ## toplam >= 255 = 255
 