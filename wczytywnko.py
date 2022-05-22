import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel('Data.xls',sheet_name="Data")
print(df.head(3))
dfcolumns={name:nr for nr, name in enumerate(df.columns)}
print(dfcolumns)
print(df.loc[:,'P2.1':'P2.5'])
print(df.iloc[:,dfcolumns['P2.1']].unique())
imSelected=[i for i in range(dfcolumns['M1'],dfcolumns['M4']+1)]
print(imSelected)
# mSelected = df.iloc[:, imSelected ].copy(); mSelected.columns
mSelected = df.iloc[:, imSelected ].copy(); mSelected.columns
print(mSelected)
#indices for M-columns. We remove some that are not good for decribe
print(mSelected.head(7))
pSelected = df.loc[:,'P1.1':'P2.18'].copy(); pSelected.columns
#imSelectedpri  =[i for i in range(dfcolumns['M1'],dfcolumns['M4']) if
# (i != dfcolumns['M2']) and (i != dfcolumns['M3']) ]
translateDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print(translateDict)
inv_translateDict = {v:k for k,v in translateDict.items()}
print(inv_translateDict)
a = mSelected.loc[:,"M1":"M4"]=mSelected.loc[:,"M1":"M4"].applymap(lambda x: translateDict[x])
print(a)
b = mSelected.loc[:,"M1":"M4"]=mSelected.loc[:,"M1":"M4"].applymap(lambda x: inv_translateDict[x])
print(b)
print(mSelected.isnull().any())
print(mSelected.isnull().sum())
n = pSelected.isnull().values.any()
print(n)
w = pSelected.isnull().sum()
print(w)
z = pSelected.dropna()
z.head(16)
print(z.head(16))
