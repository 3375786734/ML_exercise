import numpy as np

A = np.array([[1,2],[3,4]])
a,b = np.linalg.eig(A)
print('a is',a)
print('b is',b)
print(np.linalg.inv(A))
print(np.linalg.det(A))
