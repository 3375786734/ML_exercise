import numpy as np
a = np.array([[1],[2]])
a = a.reshape(1,-1)
print(a.shape)
a = np.squeeze(a)
print(a.shape)
b  =  np.array([1,2])
c = np.array([[3,4],[5,6]])
print(b.dot(c))
