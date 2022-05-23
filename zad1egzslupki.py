import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4,5]
y = [100,70,75,30,50]
y1 = [20,10,30,10]
y_pos = np.arange(len(y))

plt.figure(figsize=(10,5))

plt.bar(x[0], y[0], color = '#009999')
plt.bar(x[1], y[1], color = '#006633')
plt.bar(x[2], y[2], color = '#CCCC00')
plt.bar(x[3], y[3], color = '#FF99CC')
plt.bar(x[4], y[4], color = '#33FF33')
plt.bar(x[0], y1[0], color = '#7F00FF')
plt.bar(x[1], y1[1], color = '#00FFFF')
plt.bar(x[2], y1[2], color = '#999900')
plt.bar(x[3], y1[3], color = '#0080FF')





x = [0,1,2,3,4,5]
y2 = [120,120,120,120,120,120]
plt.plot(x,y2,color = 'green')
plt.yticks(np.arange(0, 160, 20))
plt.xticks(np.arange(0,6,1))
plt.show()
