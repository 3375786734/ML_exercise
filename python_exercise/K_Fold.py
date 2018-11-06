#交叉验证
from sklearn.model_selection import KFold
这里进行三叠,对数据先进行洗牌
kfold = KFold(n_splits = 3 ,shuffle = True,random_state = 0)
cross_validation_score(logreg,X,y,cv = kfold)

#乱序分割交叉验证
from sklearn.model_selection import ShuffleSplit

shuffle_split = ShuffleSplit(test_size = .5,train_size = .5,n_split = 10,random_state = 0)
cross_validation_score(logreg,X,y,cv = shuffle_split)

