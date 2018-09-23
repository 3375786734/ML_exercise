
'''
检查是否边界
'''
def check(N,M,x,y):
    if x>=0 and x<M and y>=0 and y<N:
        return 1;
    else :
        return 0;

'''
进行8bit LBP  编码
'''
def encode(lbp):
    cnt=0
    ans=0
    for i in range(-1,2):
        for j in range(-1,2):
            if not(i==0 and j==0):
                ans+=(1<<cnt)*lbp[i][j]
                cnt=cnt+1
    return  ans

'''
获取 pic 路径下图片的特征向量
'''
def get_feature(pic):
    from PIL import Image
    import numpy as np
    im= Image.open(pic)
    im_array=np.array(im)
    tmp= im_array
    M,N=im.size
    lbp=[[0 for col in range (3)] for row in range(3)]
    feature=[0 for i in range(0,256)]
    '''
    for i in range(0,10):
     for j in range(0,10):
            print(im_array[i][j],end=' ')
     print()
    '''
    for y in range (0,N):
        for x in range (0,M):
            for dx in range (-1,2):
                for dy in range (-1,2):
                 nx=x+dx
                 ny=y+dy
                 if check(N,M,nx,ny) and (not(dx==0 and dy==0)):
                        if im_array[ny][nx]<im_array[y][x]:lbp[dy][dx]=0
                        else :lbp[dy][dx]=1
            tmp[y][x]=encode(lbp)
            feature[tmp[y][x]]+=1
    sss=0
    #normalize it 
    for i in range(0,256):
        sss+=feature[i]
    for i in range(0,256):
        feature[i]/=sss
    
    #print("feature before",feature)
    MM=0
    mm=2
    for i in range(0,256):
        if feature[i]>MM :MM=feature[i]
        if feature[i]<mm :mm=feature[i]
    ddd=MM-mm
    for i in range(0,256):
        feature[i]=(feature[i]-mm)/ddd
    #print("feature after",feature)
    return feature

'''
对数据进行特征提取并存放到csv文件中作为raw data
'''
def get_data():
    import os
#    path="/home/li/ML/CV/data/aluminium_foil/"
#    path="/home/li/ML/CV/data/brown_bread/"
#    path="/home/li/ML/CV/data/corduroy/"
#    path="/home/li/ML/CV/data/cotton/"
#    path="/home/li/ML/CV/data/cracker/"
#    path="/home/li/ML/CV/data/linen/"
    files=os.listdir(path)
    '''
    #打印路径下的所有file的名称
    for file in files:
        print(file)
    '''
    '''
    #输出libsvm格式数据
    with open("o_data.txt","a+") as f:
        for file in files:
            feature=get_feature(path+file)
            lf=[str(i) for i in feature]
            cnt=1
            sf=''
            for i in lf:
                sf=sf+' '+str(cnt)+':'+i
                cnt+=1
            f.write('6 '+sf+'\n')
    '''


    #输出csv的逗号表达式的数据
    with open("original_data.csv","a+") as f:
        for file in files:
            feature=get_feature(path+file)
            lf=[str(i) for i in feature]
            sf=','.join(lf)
            f.write('6,'+sf+'\n')


    '''
    #在文件头追加一行列索引
    tmp=list(range(0,257))
    st=','.join([str(i) for  i in tmp])
    #print(st)
    with open("original_data.csv","r+") as f:
       content=f.read()
       f.seek(0,0)
       f.write(st+'\n'+content)
    '''

if __name__=='__main__':
    import sys
    import random
    from sklearn import svm
    import numpy as np
    import pandas as pd

    #get_data()
    #完成SVM算法并且进行交叉验证的工作
    i_data=pd.read_csv('original_data.csv')
    #clf=svm.SVC(decision_function_shape='ovo')
    x=np.array([list(i_data['1'])])
    cols=i_data.columns
    for i in cols[2:]:
        x=np.r_[x,np.array([list(i_data[i])])]
    y=np.array(list(i_data['0']))
    x=x.T
    #x=x[0:162]
    #y=y[0:162]
    #metrics是评估模块，例如准确率等
    from sklearn import metrics
    from sklearn.model_selection import cross_val_predict
    
    clf=svm.SVC(C=32,gamma=0.5,kernel='rbf',decision_function_shape='ovo')
    #10折交叉验证,cross_val_predict返回的是estimator的分类结果，用于和实际数据比较
    y_pred=cross_val_predict(clf,x,y,cv=10)
    print("data with 10folds, precision is:",metrics.accuracy_score(y,y_pred))
    #print("y",y)
    #print("y_pri",y_pred)
    
        
    
    '''
    下面是使用libsvm所做没能完成的工作
    '''
    '''
    path ='/home/li/Downloads/libsvm-3.23/python'
    sys.path.append(path)
    from svmutil import *
    y,x= svm_read_problem('o_data.txt')
    sz=len(y)
    iid = list(range(0,sz))
    slice=random.sample(iid,sz//2)
    x_train={}
    x_pre={}
    y_train=[]
    y_pre=[]

    #这一步svm_train返回的是一个model
    m=svm_train(y[0:sz-10],x[0:sz-10],'-c 5')
    #用model - m在x上做预测并返回精度
    p_label,p_acc,p_val= svm_predict(y[sz-10:],x[sz-10:],m)
    print(p_label,p_acc,p_val)
    '''
