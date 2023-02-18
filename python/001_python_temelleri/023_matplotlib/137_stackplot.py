import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


yil = [2011,2012,2013,2014,2015,2016,2017,2018]
oyuncu1 = [8,4,3,6,2,1,8,9]
oyuncu2 = [12,1,0,19,4,9,3,11]
oyuncu3 = [1,3,23,12,17,19,3,59]

plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors = ["y","r","b"])
plt.title("yıllara göre atılan gol bilgisi")
plt.xlabel("yıl")
plt.ylabel("gol sayısı")
plt.legend()

plt.show()