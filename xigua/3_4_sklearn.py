#对率回归和10折交叉验证用到sklearn库 http://scikit-learn.org/stable/
import numpy as np
import pandas as pd
import sklearn

#iris数据
#sklearn可以用datasets方法加载iris数据集，查找数据集链接 http://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets
from sklearn import datasets
#和api介绍不一样，如果增加return_X_y=True参数，反而会报错，说明false时候已经返回了target数值
iris=datasets.load_iris()
#返回的data是数据项，target是最后一列分类结果，对率分布y只有两个取值，因此取前100个数据

x=iris.data[0:100,:]
y=iris.target[0:100]


#逻辑回归
from sklearn.linear_model import LogisticRegression
#metrics是评估模块，例如准确率等
from sklearn import metrics
from sklearn.model_selection import cross_val_predict


log_model=LogisticRegression()

#10折交叉验证,cross_val_predict返回的是estimator的分类结果，用于和实际数据比较
y_pred=cross_val_predict(log_model,x,y,cv=10)
print("iris with 10folds, precision is:",metrics.accuracy_score(y,y_pred))


#留一法
from sklearn.model_selection import LeaveOneOut
loo=LeaveOneOut()
accuracy=0
#split是leaveoneout模型的方法，把数据分隔为train和test数组
#使用0/1 loss 计算ERM损失作为精度,loo.split(x)函数非常有意思
for train,test in loo.split(x):
    log_model.fit(x[train],y[train])  #fit模型
    y_p=log_model.predict(x[test])
    if y_p==y[test]:
        accuracy+=1  
print("iris with LeaveOneOut, precision is:",accuracy/np.shape(x)[0]) 
#shape(x)是数组维度这里是(100,4)表示是100行4列,因此取出第一个元素[0]对应有100个数据



