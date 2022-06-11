import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dane = pd.read_excel("ceny2.xlsx")
ryz = dane[dane["Rodzaje towarów"] == "ryż - za 1kg"]
maka = dane[dane["Rodzaje towarów"] == "mąka pszenna - za 1kg"]
y_ryz=ryz["Wartość"]
y_maka=maka["Wartość"]
print(np.mean(y_ryz))
print(np.mean(y_maka))
x =ryz["Rok"]
plt.plot(x,y_ryz, label="ryż")
plt.plot(x,y_maka, label="mąka")
plt.grid()
plt.legend(loc="center left")
plt.xlabel("Rok")
plt.ylabel("zł")
plt.title("Ceny ryżu i mąki pszennej za 1 kg")
plt.xticks(np.arange(2010,2021,2))
plt.annotate("12345",[2010,4.25])
plt.savefig("zad2.png")
plt.show()
