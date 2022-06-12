import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel("sprzedaz14.xlsx")
maslo = df[df["Produkt"]=="Masło"]
margaryna = df[df["Produkt"]=="Margaryna"]
jogurt = df[df["Produkt"]=="Jogurt"]
ymaslo = maslo["Sprzedaż"]
ymargaryna = margaryna["Sprzedaż"]
yjogurt = jogurt["Sprzedaż"]


print(np.sum(ymaslo))
print(np.sum(ymargaryna))
print(np.sum(yjogurt))
x = maslo["Rok"]
width = 0.25
x1 = [2015,2016,2017]

bar1= plt.bar(x-width,ymaslo,width,color="r")
bar2= plt.bar(x,ymargaryna,width,color="g")
bar3= plt.bar(x+width,yjogurt,width,color="b")
plt.xlabel("ROK")
plt.ylabel('WARTOSC')
plt.title("sprzedaz14")

plt.xticks(x1)
plt.legend( (bar1, bar2, bar3), ('Masło', 'Margaryna', 'Jogurt') )
plt.show()
