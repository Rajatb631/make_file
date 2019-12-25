import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
col=[]
file = open("data.txt", 'r')
fig=plt.figure()

ax=fig.add_axes([0,0,1,1])


for j in file:
    a,b,co=map(int,j.split(","))
    x.append(a)
    y.append(b)
    col.append(co)

ax.scatter(np.array(x), np.array(y), c=np.array(col))
ax.set_title('scatter plot')
plt.show()