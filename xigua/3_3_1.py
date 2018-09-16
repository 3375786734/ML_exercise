import numpy as np
import matplotlib.pyplot as plt  
import pandas as pd


#使用sklearn 库做回归#
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


# load the CSV file as a numpy matrix
data_original = pd.read_csv('xg3.csv')

# separate the data from the target attributes
#由于data_original 对应的tuple,只有转化成list才可读
X = np.array([list(data_original['density']),list(data_original['suger']),[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
y = list(data_original['good'])
X=X.T


#特别注意的是,由上面方法得到的X是横放着的,我们通常取元素,或者使用sklearn库函数都是竖着放的




"""
for i in range(17):
    if y[i]==0:
        X_good.append(X[i])
    if y[i]==1:
        X_bad.append(X[i])
print(X_good)
"""
#这里由于array给的是横着放的1...17,而我们要的是竖着放取前8行
X_bad=X[:8]
X_good=X[8:]
print(X_bad,'\n',X_good)
# generalization of test and train set
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.5, random_state=0)


# model training
log_model = LogisticRegression() 
log_model.fit(X_train, y_train) 

print(log_model.coef_)

# model testing
y_pred = log_model.predict(X_test)
# summarize the accuracy of fitting
print(metrics.confusion_matrix(y_test, y_pred))
print(metrics.classification_report(y_test, y_pred))


#创建一个figure
plt.figure(1)

# Put the result into a color plot
plt.title('watermelon_3a')  
plt.xlabel('density')
plt.ylabel('ratio_sugar')  
#这里y对应的index为0,那么就是bad,否则为good
plt.scatter(X_good[:,0],X_good[:,1] ,marker = 'o', color = 'k', s=100, label = 'bad')
plt.scatter(X_bad[:,0],X_bad[:,1], marker = 'o', color = 'g', s=100, label = 'good')
#这句话指bad和good分别用什么颜色代替画在左上角还是右上角
plt.legend(loc = 'upper right')  
#记住要show图片
plt.show()
