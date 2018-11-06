'''
最简单网格暴力枚举,按数量级进行
'''
#以SVC的rbf核参数gamma和C为例,最直接的搜索方法
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split 
#先将数据分为测试与验证
X_train,X_test,y_train,y_test  = train_test_split(X,y,random_state=0)
best_score = 0
for gamma in [0.001,0.01,0.1,1,10,100]:
    for C in [0.001,0.01,0.1,1,10,100]:
        svm = SVC(gamma = gamma ,C = C)
        svm.fit(X_train,y_train)
        score = svm.score(X_test,y_test)
        if score >best_score:
            best_score = score
            best_para = {'C':C,'gamma':gamma}
print("best_para: ",best_para)

'''
交叉验证网格搜索
Note:  这里将数据分为: 训练验证集+测试集 , 训练验证集= 训练集+验证集
       其中网格搜索中交叉验证使用训练验证集
'''
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
X_train_val , X_test,y_train_val,y_test = train_test_split(X,y,random_state= 0)
best_score = 0
for gamma in [0.001,0.01,0.1,1,10,100]:
    for C in [0.001,0.01,0.1,1,10,100]:
        svm = SVC(gamma = gamma ,C = C)
        score = cross_val_score(svm,X_train_val,y_train_val,cv=5)
        score = np.mean(score)
        if(score>best_score):
            best_score = score
            best_para = {'C':C,'gamma':gamma}
print("best_para: ", best_para)
#这里使用上面网格搜索好的数据
svmf = SVC(**best_para)
svmf.fit(X_train_val,y_train_val)
#使用测试集进行测试
print("score :",svmf.score(X_test,y_test))
#在整个数据集上进行交叉验证
scores = cross_val_score(svmf,X,y,cv = 5)
print("score on cv:" ,np.mean(scores))


'''
接下来使用字典参数代替for循环
'''
para_grid  = {'C':[0.001,0.01,0.1,1,10,100], 'gamma':[0.001,0.01,0.1,1,10,100]}
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
grid_search = GridSearchCV(SCV(),pram_grid,cv = 5)
#先搜索得到最优参数
'''
其中有 .best_params_ 获取最优参数,有.fit直接使用该模型进行拟合,所以可以将grid_search看成是最优参数的一个模型
'''
#训练结束时候直接进行cv
scores = cross_val_score(grid_srearch,X,y,cv = 10)
print(scores)

