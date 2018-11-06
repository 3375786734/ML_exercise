def read_data(path):
    import numpy as np
    import pandas as pd
    import sys

    i_data=pd.read_csv(path)

    x=np.array([list(i_data['1'])])
    data_cols=i_data.columns
    for i in data_cols[2:]:
        x=np.r_[x,np.array([list(i_data[i])])]
    y=np.array(list(i_data['0']))
    x=x.T
    return x,y

'''
@input:feature x and label y
@output:accuracy_score
'''
def svm_solve(x,y,cas):
    from sklearn import svm
    #metrics是评估模块，例如准确率等
    from sklearn import metrics
    from sklearn.model_selection import cross_val_predict
    
    clf=svm.SVC(C=32,gamma=0.5,kernel='rbf',decision_function_shape='ovo')
    #10折交叉验证,cross_val_predict返回的是estimator的分类结果，用于和实际数据比较
    y_pred=cross_val_predict(clf,x,y,cv=10)
    if cas ==-1 :
        print("Case with no guassian noisy:")
    else :
        print("Case sigma %d: "%(10**cas))
    print("data with 10folds, precision is:",metrics.accuracy_score(y,y_pred))

'''
对数据进行特征提取并存放到csv文件中作为raw data
注意的是文件名后面要加上'/'因为listdir没有'/'
'''
def get_data(rpath,wpath):
    import os
    path = rpath
    files=os.listdir(path)
    cnt = 1
    for image_class in files:
        files = os.listdir(path+image_class)
        print("here "+str(cnt))
        for file in files:
                feature = get_feature(path+image_class+'/'+file)
                write_data(feature,cnt,wpath)
        cnt += 1
    add_head(wpath)

def write_data(feature,label,path):

    #输出libsvm格式数据
    with open(path,"a+") as f:
        lf=[str(i) for i in feature]
        cnt=1
        sf=''
        for i in lf:
            sf=sf+' '+str(cnt)+':'+i
            cnt+=1
        f.write('6 '+sf+'\n')
    '''
    #输出csv的逗号表达式的数据
    with open(path,"a+") as f:
        lf=[str(i) for i in feature]
        sf=','.join(lf)
        f.write(str(label)+','+sf+'\n')
    '''
    #add_head(path)
    
def add_head(path):

    #在文件头追加一行列索引这里向量是256dim的
    tmp=list(range(0,257))
    st=','.join([str(i) for  i in tmp])
    #print(st)
    with open(path,"r+") as f:
       content=f.read()
       f.seek(0,0)
       f.write(st+'\n'+content)

'''
@para: image-path

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
    #打印像素
    for i in range(0,10):
     for j in range(0,10):
            print(im_array[i][j],end=' ')
     print()
    '''

    im_array = add_noisy(im_array,N,M,"Guass",60)
    
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
    sum_feature=0
    #normalize it
    for i in range(0,256):
        sum_feature+=feature[i]
    for i in range(0,256):
        feature[i]/=sum_feature

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


def add_noisy(im_array,N,M,kind,sigma):
    import numpy as np
    SampleNum = 10001
    distrubute = sigma*np.random.randn(SampleNum)
    if kind == "Guass":
        for i in range(0,N):
            for j in range(0,M):
                tmp = im_array[i][j]
                tmp = tmp + distrubute[random.randint(0,SampleNum-1)]
                if tmp<0: tmp = 0 
                if tmp>255:tmp = 255
                im_array[i][j] = int(tmp)
    return im_array


if __name__=='__main__':
    import sys
    import numpy as np
    import pandas as pd
    import random
    #完成特征提取的函数
    get_data("/home/li/ML/CV/data/","Oridata_sigma_60.csv")
    path ='Oridata_sigma_60.csv'
    #x,y = read_data(path)
    #svm_solve(x,y,2)
    '''
    for i in range(-1,3):
        if i>=0:
            path = 'Oridata_sigma_'+str(10**i)+'.csv'
            x,y=read_data(path)
            svm_solve(x,y,i)
        else:
            path = 'original_data.csv'
            x,y = read_data(path)
            svm_solve(x,y,i)
    '''
