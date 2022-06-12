import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D', 'E'
sizes = [29.7, 17.4, 17.4, 18.1, 17.4]
explode = (0, 0.1, 0, 0, 0)
colors = 'cyan', 'brown', 'grey', 'orange', 'blue'

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=45, colors=colors)
ax1.axis('equal')
plt.title("Tytuł W")
plt.savefig("kolo.pdf")
plt.show()
