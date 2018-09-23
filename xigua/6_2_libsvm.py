import sys
path ='../../Downloads/libsvm-3.23/python'
sys.path.append(path)
from svmutil import *
y,x = svm_read_problem('heart_scale')
#这一步svm_train返回的是一个model
m=svm_train(y[:200],x[:200],'-c 4')
#用model - m在x上做预测并返回精度
p_label,p_acc,p_val= svm_predict(y[200:],x[200:],m)
print(p_label,p_acc,p_val)
