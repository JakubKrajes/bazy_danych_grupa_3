import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
wartosci = list(np.random.randint(low = 10,high=50,size=5))
wartosci2 = list(np.random.randint(low = -50,high=0,size=5))
lista = ["A","B","C","D","E"]
fig, ax = plt.subplots()
x1= [10,20,30,40]

plt.subplot(1, 2, 1)
plt.barh(lista, wartosci, color=['#9CE5E4', '#FB9797', 'orange', 'grey', 'purple'])
plt.title("Wykres lewy")

plt.subplot(1, 2, 2)

plt.barh(lista, wartosci2, color=['#E965DB', 'cyan', 'cyan', 'brown', '#545A2E'])
plt.title("Wykres Prawy")

plt.show()
