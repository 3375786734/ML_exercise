import numpy as np
a = [[[1,2,3],[4,5,6]],[[7,8,9],[11,12,13]]]
print(np.array(a).shape)
print(np.array(np.concatenate(a,axis=1)))
print("here")
b = [1,2,3,4,5,6,7,8,9,10]
print(np.clip(b,np.percentile(b,1),np.percentile(b,80)))