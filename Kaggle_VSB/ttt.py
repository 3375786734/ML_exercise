import numpy as np
a = [[[1,2,3],[4,5,6]],[[7,8,9],[11,12,13]]]
print(np.array(a).shape)
print(np.array(np.concatenate(a,axis=1)))
