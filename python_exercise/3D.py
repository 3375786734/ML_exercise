from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
#对X,Y进行网格划分,取点,这里arange()的含义是-4->4之间步长为0.25的等差数列
X = np.arange(-1,0.5,0.25)
Y = np.arange(-2,1,0.25)

#注意这里meshgrid的作用,相当于将x,y按坐标划分,然后,每个小格子按坐标排列
#例如x[0][0]= -1, y[0][0]= -2;
X,Y = np.meshgrid(X,Y)
print("X:")
print(X)
print("Y:")
print(Y)
R = np.sqrt(X**2+Y**2)
Z = np.sin(R)

ax.plot_surface(X,Y,Z,rstride = 1,cstride =1,cmap='rainbow')
plt.show()

