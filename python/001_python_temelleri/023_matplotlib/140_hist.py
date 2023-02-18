import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



yaslar = [22,55,62,45,21,22,34,42,4,42,2,105,102,95,85,110,120,65,55,111,115,48]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("yaş grupları")
plt.ylabel("kişi sayısı")
plt.title("histogram")



plt.show()