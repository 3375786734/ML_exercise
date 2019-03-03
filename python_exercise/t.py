import numpy as np
#print(np.arange(10))

a = []
b = [4,5,6]
c = [7,8,9]
d = [np.asarray([1,2]),[3,4],[5,6]]
print(d)
e = np.concatenate(d)
print(e)
#Note that: typically append should start at a null list.
a.append(b)
a.append(c)
print(a)
f = np.concatenate(a,axis =1)
print(f)
