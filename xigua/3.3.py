import numpy as np
#linalg是线性代数模块，包括求范数
from numpy import linalg
#pandas是导入表格数据的方法，详见http://codingpy.com/article/a-quick-intro-to-pandas/
import pandas as pd
#定义excel文件的读取路径
inputfile='/Users/huatong/PycharmProjects/Data/xiguaexcel.xls'
#读取数据文件，参数只填路径就可以
data_original=pd.read_excel(inputfile)



#βTx实际上是β乘x的转置。这里的beta是书里已经转置过的，x是第一行密度，第二行含糖量的矩阵，下面的x也就是书里的x^=(x;1)的转置
#numpy array用于构造数组。read_excel读取出的数据是元组结构tuple。列表可读写,元组只读。list用于把元组转换成列表，也就是把表格数据打散。单引号指定某一列
x=np.array([list(data_original['density']),list(data_original['suger']),[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
#y是是否好瓜，因为后面βTx的结果是一行，y也就是一行了
y=np.array(list(data_original['good']))
#定义初始参数，注意这个beta是书里β=(w;b）的转置
beta=np.array([[0],[0],[1]])
#3.27式的l(β）,是上一次迭代的l值
old_l=0
#n是迭代次数
n=0

#迭代
while 1:
    #numpy dot是矩阵相乘，numpy T是求转置矩阵，因为β转置后只有一行，只需要转置后第一行与x^相乘
    beta_T_X=np.dot(beta.T[0],x)  #python没有数组概念，后面的beta_T_x[i]也就是列表中i元素的数值
    cur_l=0  #初始化l值，以下求和
    for i in range(17):
        cur_l=cur_l+(-y[i]*beta_T_X[i]+np.log(1+np.exp(beta_T_X[i]))) #式3.27，目标是求使得这个值最小的β

    #迭代终止条件
    if np.abs(cur_l-old_l)<=0.000001: #abs求绝对值，相差小于0.000001认为收敛
        break

    #牛顿法更新β，根据式3.29到3.31
    n=n+1
    old_l=cur_l
    dbeta=0  #一阶导，下面是二阶导
    d2beta=0
    for i in range(17):
        #这里的x是转置后的，因此这一步要再转置回来
        dbeta=dbeta-np.dot(np.array([x[:,i]]).T,(y[i]-(np.exp(beta_T_X[i])/(1+np.exp(beta_T_X[i])))))
        d2beta=d2beta+np.dot(np.array([x[:,i]]).T,np.array([x[:,i]]).T.T)*(np.exp(beta_T_X[i])/(1+np.exp(beta_T_X[i])))*(1-(np.exp(beta_T_X[i])/(1+np.exp(beta_T_X[i]))))
    beta=beta-np.dot(linalg.inv(d2beta),dbeta)  #inv是矩阵求逆
print('模型参数是：',beta)
print('迭代次数：',n)
