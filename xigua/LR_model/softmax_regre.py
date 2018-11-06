'''
原始softmax定义
'''
scores = np.array([123, 456, 789]) # example with 3 classes and each having large scores 
scores -= np.max(scores) # scores becomes [-666, -333, 0] 
p = np.exp(scores) / np.sum(np.exp(scores))

'''
softmax_regression;
example: V = [-3,2,-1,0]有四个类别,分别对应的类别值
@para:
 - W: A numpy array of shape (D, C) containing weights.
 - X: A numpy array of shape (N, D) containing a minibatch of data.
 - y: A numpy array of shape (N,) containing training labels; y[i] = c means
   that X[i] has label c, where 0 <= c < C.这里是多分类的标签
 - reg: (float) regularization strength
@return loss and gradient
'''
def softmax_regression_v1(W, X, y, reg): 

loss = 0.0
#这一步初始化一个和W一样的全零矩阵
dW = np.zeros_like(W)

#得到所有的样本的[0]行 [1]列,W.shape[1]是因为类别数正好对应x_i的行数
    num_train = X.shape[0]
    num_classes = W.shape[1]

    for i in range(num_train):

    #得到 s_i=Wx_i的原始计算
    scores = X[i,:].dot(W)
    scores_shift = scores - np.max(scores)
    right_class = y[i]
    
    #计算对数soft max 损失函数,
    loss += -scores_shift[right_class] + np.log(np.sum(np.exp(scores_shift)))
    #get gradient
    for j in range(num_classes):
        softmax_output = np.exp(scores_shift[j])/np.sum(np.exp(scores_shift))
        if j == y[i]:
            dW[:,j] += (-1 + softmax_output)*X[i,:]
        else:
            dW[:,j] += softmax_output * X[i,:]


    loss /= num_train    
    #l_2 regression
    loss += 0.5*reg*np.sum(W*W)
    dW /= num_train
    dW += reg*W
    return loss,dW

def softmax_loss_vectorized(W, X, y, reg): 
  # Initialize
  loss = 0.0 
  dW = np.zeros_like(W) 
  num_train = X.shape[0] 
  num_classes = W.shape[1] 
  scores = X.dot(W)



  #这一步注意max的用法,参见exercise
  #axis = 1 取出每行的最大值,也就是对应每个样本(每一行)的所有feature中值最大的那一个,然后reshape成矩阵
  #遍历每一列的所有元素都减去相应位置的最大值,因为这里reshape成列
  scores_shift = scores - np.max(scores, axis = 1).reshape(-1,1)

  #这里的乘法和除法都对应的   element wise!!

  #sum对每一行求和,然后对每一列的scores_shitft元素相除
  softmax_output = np.exp(scores_shift) / np.sum(np.exp(scores_shift), axis=1).reshape(-1,1) 
  
  #首先range取出所有行,然后取出每个y[i]对应真实标签的列,根据loss function的定义,十分简介.
  loss = -np.sum(np.log(softmax_output[range(num_train), list(y)]))
  #正则化
  loss /= num_train loss += 0.5 * reg * np.sum(W * W) 
  dS = softmax_output.copy()
  dS[range(num_train), list(y)] += -1 
  dW = (X.T).dot(dS)
  dW = dW / num_train + reg * W 
  return loss, dW


#注意怎么测试时间,正则化因子很小,%e,%f输出
tic = time.time() 
loss_naive, grad_naive = softmax_regreesion_v1(W, X_train, y_train, 0.000005) 
toc = time.time() 
print('naive loss: %e computed in %fs' % (loss_naive, toc - tic))
