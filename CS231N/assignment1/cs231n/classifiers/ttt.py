import numpy as np
a = np.array([1,2,3,4])
b = np.array([1,1,3,1])
print(np.where((a!=1)&(b==1)).shape)
