import numpy as np
import tqdm as tqdm
a = [[1,2],[3,4]]
b = []
b.append(a)
print(np.array(b).shape)
b = np.concatenate(b)
print(np.array(b).shape)
cnt = 0
'''
for i in tqdm((range(1,int(1e4),1)):
    cnt += 1
'''
print(np.transpose(a))
