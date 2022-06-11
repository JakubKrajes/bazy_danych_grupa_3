import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dane = pd.read_csv("cechy41.csv", sep=";", decimal=",")
cecha1 = dane["Cecha1"]
cecha2 = dane["Cecha2"]
cat = [0, 50, 100, 150, 200]
p1 = pd.cut(cecha1, bins=cat)
koszyk1 = pd.value_counts(p1, sort=False)
p2 = pd.cut(cecha2, cat)
koszyk2 = pd.value_counts(p2, sort=False)
x = np.arange(4)

print(x)
plt.subplot(1, 2, 1)
plt.barh(x, koszyk1, color='red')
plt.xlabel("Cecha1",color='red')
plt.xticks(np.arange(0,240,50))
plt.subplot(1, 2, 2)
plt.barh(x,koszyk2,color='green')
plt.xlabel("Cecha2", color='green')
plt.xticks(np.arange(0,240,50))
plt.show()
