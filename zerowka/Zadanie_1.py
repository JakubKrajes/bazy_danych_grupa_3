import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import scipy.integrate as integrate
import scipy.special as special
import sympy

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

x = np.linspace(0.5, 10, 100)
y = np.log(2*x)
y1 = -4*x + 2
y2 = 2*np.cos(x)
fig, axs = plt.subplots()

axs.set_ylim([-3, 3])
axs.plot(x, y, ls='--' ,label='log(2x)', color = "green")
axs.plot(x, y1,ls='dotted', label='-4x+2', color = "red")
axs.plot(x, y2,ls='-.', label='2cos(x)', color = "blue")
axs.set_xlabel("oś pozioma")
axs.set_ylabel("oś pionowa po lewej stronie")
plt.title("Wykresy - kilka")
plt.legend()
plt.grid()
plt.savefig("3wykresy.png")
plt.show()
