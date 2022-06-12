import numpy as np
import matplotlib.pylab as plt

#prepare data
x = np.linspace(5, 15, 100)
x1 = np.linspace(0, 2*np.pi,100)
y1 = 3*x**2+2*x+7
y2 = -4*x+2
y3 = 2*np.cos(x1)


fig, axs = plt.subplots()

plt.grid(which="both")


axs.plot(x, y1, ls='--', c="grey", label = "3x^2+2x+7")
axs.plot(x, y2, ls='-.', c="red", label = "-4x+2")
axs.legend(loc='upper center')
axs.set_xlabel("oś pozioma")
axs.set_ylabel("oś pionowa po lewej stronie")



ax2 = axs.twinx()

ax2.plot(x, y3, ls="dotted", c = "blue", label = "2cos(x)")
ax2.legend(loc='center left')
ax2.set_ylabel("oś pionowa po prawej stronie")


plt.title("Wykresy - kilka")



plt.show()