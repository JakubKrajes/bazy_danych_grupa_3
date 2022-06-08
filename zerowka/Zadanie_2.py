import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import scipy


df = pd.read_excel("ceny41.xlsx")

m = df.loc[df["Rodzaje towarów i usług"]== "marchew - za 1 kg"]
c = df.loc[df["Rodzaje towarów i usług"]== "cebula - za 1 kg"]
z = df.loc[df["Rodzaje towarów i usług"]== "ziemniaki - za 1 kg"]
cenam  = m["Wartosc"]
miesiacm = m["Miesiące"]
cenac  = c["Wartosc"]
miesiacc = c["Miesiące"]
cenaz  = z["Wartosc"]
miesiacz = z["Miesiące"]

print(m)
print(cenam)


print("Marchew za 1 kg : ", m["Wartosc"].mean())
print("Cebula za 1 kg : ", c["Wartosc"].mean())
print("Ziemniaki za 1 kg : ", z["Wartosc"].mean())

fig, axs = plt.subplots(figsize=(15,5))
axs.plot(miesiacm, cenam, ls='--' ,label='Marchew', color = "orange")
axs.plot(miesiacc, cenac, ls='-.' ,label='Cebula', color = "yellow")
axs.plot(miesiacz, cenaz, ls='dotted' ,label='Ziemniaki', color = "brown")
axs.set_xlabel("Miesiące")
axs.set_ylabel("Ceny w zł")
plt.text(0,1, "162647")
plt.grid()
plt.legend()
plt.title("Cena towaru za 1 kg rok 2017")
plt.savefig("excel.jpg")

plt.show()
