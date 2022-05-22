import numpy as np
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import *

df=pd.read_excel('zarobki (1).xls')
#print(df)

x = list(df['Imiona'])
y = list(df["Zarobki"])
plt.figure(figsize=(5,5))
plt.style.use('seaborn')
plt.bar(x,y,color="yellow")
plt.title("Excel sheet to Scatter Plot")
plt.show()
