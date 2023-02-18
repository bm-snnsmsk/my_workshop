import matplotlib.pyplot as plt
import numpy as np

# x = [1,2,3,4]
# y = [5,19,21,75]
# # plt.plot(x)
# plt.axis([0,7,0,76])
# plt.plot(x,y,"--g")
# plt.plot(x,y,"1--r")
# plt.plot(x,y,"o:b")

# plt.title("Grafik başlığı")
# plt.xlabel("x label")
# plt.ylabel("y label")


x = np.linspace(0,2,100)
# plt.plot(x,x,label="linear")
# plt.plot(x,x**2,label="quadratic",color="pink")
# plt.plot(x,x**3,label="cubic")
# plt.legend()


# fig,axs = plt.subplots(3)
# axs[0].plot(x, x, color = "red")
# axs[0].set_title("linear")
# axs[1].plot(x, x**2, color = "blue")
# axs[1].set_title("quadratic")
# axs[2].plot(x, x**3, color = "yellow")
# axs[2].set_title("cubic")
# plt.tight_layout()


fig,axs = plt.subplots(2,2)
fig.suptitle("grafik ana başlığı")
axs[0,0].plot(x, x, color = "red")
axs[0,0].set_title("linear")
axs[0,1].plot(x, x**2, color = "blue")
axs[0,1].set_title("quadratic")
axs[1,0].plot(x, x**3, color = "yellow")
axs[1,0].set_title("cubic")
axs[1,1].plot(x, x**4, color = "purple")
axs[1,1].set_title("four")
plt.tight_layout()








plt.show()