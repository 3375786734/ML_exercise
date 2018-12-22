from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import math
pi = math.acos(-1)
a = pi 
b = 2*pi
fig = plt.figure()
ax = Axes3D(fig)

t = np.arange(0,a,0.1)
u = np.arange(0,2*pi,0.1)
v = np.arange(0,2*pi,0.1)

t,u,v = np.meshgrid(t,u,v)

x = t*np.cos(u)
y = (b+t*np.sin(u))*np.cos(v)
z = (b+t*np.sin(u))*np.sin(v)

ax.plot_surface(rstride = 1,cstride =1, cmap ='rainbow')
plt.show()
