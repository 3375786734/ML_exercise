import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt

#采样点个数
SampleNum = 1000

#对应中心在3的位置
mu = 3
sigma = 0.1
np.random.seed(0)

#得到的是坐标值.都是接近mu的
distribute = np.random.normal(mu,sigma,SampleNum)
#print(distribute)
#可视化,生成一个 2*2的子图,当前是第一幅
plt.subplot(2,2,1)
#统计x出现的频率
plt.hist(distribute,30)


#下面是使用单位正态分布生成的,注意到这里使用的基本变换公式
distribute = sigma*np.random.randn(SampleNum)+mu
plt.subplot(2,2,2)
plt.hist(distribute,30)

sigma = 10
mu = 0
distribute = sigma*np.random.randn(SampleNum)+mu
plt.subplot(2,2,3)
plt.hist(distribute , 100)

# 二维正态分布因为Y = AX++mu 的Cov(Y) = AA'=sigma,因此对sigma进行cholesky分解就可以得到A
mu = np.array([[1, 5]])
Sigma = np.array([[1, 0.5], [1.5, 3]])
R = cholesky(Sigma)
s = np.dot(np.random.randn(SampleNum, 2), R) + mu
plt.subplot(2,2,4)
# 注意绘制的是散点图，而不是直方图
plt.plot(s[:,0],s[:,1],'+')


plt.show()

