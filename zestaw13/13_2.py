import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_excel("ceny13.xlsx")

x=df.groupby("Rodzaje towarów")
dzem=(x.get_group("dżem - za 360g"))
print(dzem)
print("miut", dzem["Wartosc"].mean())

proszek=(x.get_group("miód pszczeli - za 400g"))
print("proszek", proszek["Wartosc"].mean())

miut = df[df["Rodzaje towarów"] == "dżem - za 360g"]
proszek = df[df["Rodzaje towarów"] == "miód pszczeli - za 400g"]

y_miut=miut["Wartosc"]
y_proszek=proszek["Wartosc"]

x=miut["Rok"]

plt.plot(x,y_miut, label="miut")
plt.plot(x,y_proszek, label="proszek")
plt.grid()
plt.xlabel("lata")
plt.ylabel("cena")
plt.title("Towary")
plt.legend(loc="center left")
plt.annotate("12345",[2014,12])
plt.xticks(np.arange(2014,2018,1))
plt.savefig("miodyprochy.pdf")
plt.show()