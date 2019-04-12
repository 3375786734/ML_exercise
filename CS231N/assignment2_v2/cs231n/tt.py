import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([2,1])
print(*a.shape)
c = np.pad(a,((1,),(1,)),mode = 'constant')
print(c)
d = a +b[:,None]
print(d)
