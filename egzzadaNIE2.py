import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_excel("mieszkania1.xlsx")

indywidualne=dane[dane["Formy budownictwa"] =="indywidualne"]
spółdzielcze=dane[dane["Formy budownictwa"]=="spółdzielcze"]
komunalne=dane[dane["Formy budownictwa"]=="komunalne"]
wartosc=dane["Wartość"]
print(dane)
print(komunalne)
width = 0.25
x=indywidualne["Rok"]
y_indywidualne=indywidualne["Wartość"]
bar1=plt.bar(x,y_indywidualne, width, color='r')
y_spółdzielcze=spółdzielcze["Wartość"]
bar2=plt.bar(x+width,y_spółdzielcze, width, color='g')
y_komunalne=komunalne["Wartość"]
bar3=plt.bar(x+width*2,y_komunalne, width, color='b')

plt.xlabel("ROK")
plt.ylabel('WARTOSC')
plt.title("FORMY BUDOWNICTWA")

plt.xticks(x+width,x)
plt.yticks(np.arange(0,70000,5000))
plt.legend( (bar1, bar2, bar3), ('Indywidualne', 'spółdzielcze', 'komunalne') )
plt.show()









