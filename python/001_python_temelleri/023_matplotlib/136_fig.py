import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(-10, 9, 20)
y = x ** 3
z = x ** 2

# figure = plt.figure()

# axes = figure.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y,"b")
# axes.set_xlabel("X Axis")
# axes.set_ylabel("Y axis")
# axes.set_title("Cube")

# axes2 = figure.add_axes([0.12,0.6,0.3,0.3])
# axes2.plot(x,z,"--r")
# axes2.set_xlabel("X Axis")
# axes2.set_ylabel("Y axis")
# axes2.set_title("Square")

# axes = figure.add_axes([0,0,1,1])

# axes.plot(x,z,label="square")
# axes.plot(x,y,label="cube")
# axes.legend(loc=2)

fig, axes = plt.subplots(2,1)
axes[0].plot(x,y)
axes[0].set_title("cube")
axes[1].plot(x,y)
axes[1].set_title("square")
plt.tight_layout()
fig.savefig("fig1.png")
fig.savefig("fig1.pdf")



plt.show()