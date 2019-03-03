import numpy as np
from sklearn.model_selection import KFold,StratifiedKFold


X=np.array([
  [1,2,3,4],
  [11,12,13,14],
  [21,22,23,24],
  [31,32,33,34],
  [41,42,43,44],
  [51,52,53,54],
  [61,62,63,64],
  [71,72,73,74]
  ])

y=np.array([1,1,0,0,1,1,0,0])
sfolder = StratifiedKFold(n_splits=4,random_state=0,shuffle=False).split(X,y)
'''
print("first case")
for x  in sfolder:
    print(x)
print("second case")
'''
for idx,(X_index,y_index) in enumerate(sfolder):
    print("fold {}".format(idx))
    print(X[X_index])
    print(y[y_index])
