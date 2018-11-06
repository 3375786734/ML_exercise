import numpy as np

a = np.array([[1,2],[3,4]])
#这里如果是0表示列的最大值,1为行的最大值
print(np.max(a,axis=0))

#注意这里返回的不是矩阵而是向量,因此如果需要矩阵需要reshape
print(np.max(a,axis=0).size)

print(np.max(a,axis=0).reshape(1,-1))

print(a-np.max(a,axis=1).reshape(1,-1))
