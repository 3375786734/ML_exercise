import numpy as np 

a = np.arange(16)
print(a)
a = a.reshape(-1,1)
print(a)
c = np.array_split(a,4)
print(c)
print(c[1])
print(np.vstack(c[0:2]+c[2:]))
