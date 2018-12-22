import plotly
import plotly.figure_factory as FF
import plotly.graph_objs as go
import numpy as np
from scipy.spatial import Delaunay

## Draw torus
u = np.linspace(0, 2*np.pi, 15)
v = np.linspace(0, 2*np.pi, 15)
U,V = np.meshgrid(u,v)
u = U.flatten()
v = V.flatten()

x = (3 + (np.cos(v)))*np.cos(u)
y = (3 + (np.cos(v)))*np.sin(u)
z = np.sin(v)

X = (3 + (np.cos(V)))*np.cos(U)
Y = (3 + (np.cos(V)))*np.sin(U)
Z = np.sin(V)

points2D = np.vstack([u,v]).T
tri = Delaunay(points2D)
simplices = tri.simplices

torus = FF.create_trisurf(x=x, y=y, z=z, simplices=simplices, title="Torus", aspectratio=dict(x=1, y=1, z=0.3),plot_edges=True, width=1000)

fig = dict(data = torus)
plotly.offline.plot(fig)
