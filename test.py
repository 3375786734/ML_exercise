import mylib.IO_Interface.IOPY as iopy
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV, StratifiedKFold
ioer = iopy.io_py()
df = ioer.read_data('data.csv','csv')
FOLD_NUM = 5
X,y = df[:,1::],df[:,0:1:]
splits = list(StratifiedKFold(n_splits = FOLD_NUM,shuffle = True).split(X,y))
preds_val = []
y_val = []
paras ={'task': 'train',
        'boosting_type': 'gbdt',  # 设置提升类型
        'objective': 'regression', # 目标函数
        'metric': {'l2', 'auc'},  # 评估函数
        'num_leaves': 31,   # 叶子节点数
        'learning_rate': 0.05,  # 学习速率
        'feature_fraction': 0.9, # 建树的特征选择比例
        'bagging_fraction': 0.8, # 建树的样本采样比例
        'bagging_freq': 5,  # k 意味着每 k 次迭代执行bagging
        'verbose': 1 # <0 显示致命的, =0 显示错误 (警告), >0 显示信息
        }
for idx, (train_idx,val_idx) in enumerate(splits):
    '''
    print("Now fold %d"%(idx+1))
    print("train idx is :",train_idx)
    print("val_idx is :",val_idx)
    '''
    
    train_X,train_y,val_X,val_y = X[train_idx],y[train_idx],X[val_idx],y[val_idx]
    train_y,val_y = np.concatenate(train_y.reshape(1,-1)),np.concatenate(val_y.reshape(1,-1))
    lgb_train_set = lgb.Dataset(np.array(train_X),np.array(train_y),free_raw_data= False)
    lgb_valid_set = lgb.Dataset(np.array(val_X),np.array(val_y),reference=lgb_train_set,free_raw_data = False)
    gbm =lgb.train(paras,lgb_train_set,num_boost_round = 20 ,valid_sets = lgb_valid_set,early_stopping_rounds =5)
    gbm.save_model("gbdt"+"{}".format(idx)+".txt")
    
