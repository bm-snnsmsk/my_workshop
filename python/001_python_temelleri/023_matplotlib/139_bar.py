import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20], label="BMV", width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,50,60,50], label="Audi",width=.5)
plt.legend()
plt.xlabel("gün")
plt.ylabel("alınan mesafe (km)")
plt.title("title bilgileri")

plt.show()