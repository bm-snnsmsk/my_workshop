import cv2
import numpy as np
import matplotlib.pyplot as plt


##------------------ zeros img in histogram START ----------------------##
# img = np.zeros((200, 200), np.uint8)
# cv2.circle(img, (100,100), 30, 255, -1)
##------------------ zeros img in histogram END ------------------------##



##------------------ foto in histogram START ----------------------##
img = cv2.imread("images/avatar4.png")
b, g, r = cv2.split(img)
# cv2.imshow("b", b)
# cv2.imshow("g", g)
# cv2.imshow("r", r)
##------------------ foto in histogram END ------------------------##












cv2.imshow("img", img)
# plt.hist(img.ravel(), 256, [0, 256])  ## verilerin yatay sıraya dizilmiş hali, renk_değeri, (renk_aralığı)
plt.hist(b.ravel(), 256, [0, 256])  ## verilerin yatay sıraya dizilmiş hali, renk_değeri, (renk_aralığı)
plt.hist(g.ravel(), 256, [0, 256])  ## verilerin yatay sıraya dizilmiş hali, renk_değeri, (renk_aralığı)
plt.hist(r.ravel(), 256, [0, 256])  ## verilerin yatay sıraya dizilmiş hali, renk_değeri, (renk_aralığı)
plt.show()


 