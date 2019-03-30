import numpy as np
a = np.array([[1],[2]])
a = a.reshape(1,-1)
print(a.shape)
a = np.squeeze(a)
print(a.shape)
b  =  np.array([1,2])
c = np.array([[3,4],[5,6]])
print(b.dot(c))
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a.dot(b))
d = [1,4,3,2]
s = np.array([0.1,0.2,0.3,0.4])
print(np.sum(a))

