import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv("transport14.csv",delimiter=";")
df = df.T
df = df.reset_index()
print(df)
motocykle = df.loc[0:6]
samochody = df.loc[7:13]
autobusy = df.loc[14:20]
fig, axs = plt.subplots()
print(motocykle[2])
x = motocykle[0]

axs.plot(x,motocykle[2],color="r")
axs.plot(x,samochody[2],color="b")
plt.ylabel("Samochody i motocykle")
plt.xlabel("lata")
ax2 = axs.twinx()
ax2.plot(x,autobusy[2],color="green")
plt.ylabel("Autobusy")
plt.title("Transport")

plt.show()