import sys
path ='../../Downloads/libsvm-3.23/python'
sys.path.append(path)
from svmutil import *
y,x = svm_read_problem('heart_scale')
m=svm_train(y[:200],x[:200],'-c 4')
p_label,p_acc,p_val= svm_predict(y[200:],x[200:],m)
print(p_label,p_acc,p_val)
