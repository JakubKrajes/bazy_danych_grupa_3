import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("turystyka13.csv",header=0,delimiter=";", decimal=".")
print(df)
print(df["hotele.1"])
df=df.T

print(df)
df=df.reset_index()
print(df)

hotele=df.loc[0:1]
motele=df.loc[2:3]
pensjonaty=df.loc[4:5]


yh=[2540, 2592]
ym=[110,110]
yp=[384,700]

plotdata=pd.DataFrame({"Hotele":yh,"Motele":ym,"Pensonaty":yp},index=[2017,2018])



plotdata.plot(kind="bar")
plt.grid()
plt.legend()
plt.xlabel("Lata")
plt.ylabel("Wartości")
plt.title("Wykresy hotele motele pensjonaty")

plt.savefig("Wykres.jpg")
plt.show()



