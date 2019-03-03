import numpy as np
a = [[1,2],[3,4]]
b = []
b.append(a)
print(np.array(b).shape)
b = np.concatenate(b)
print(np.array(b).shape)
