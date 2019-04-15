import numpy as np
a = np.array([[1,2],[3,4]])
b = a[range(a.shape[0]),range(a.shape[0])]
print(b.shape)
c = np.diag(a)
print(c)
d = {}
