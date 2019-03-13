import lightgbm as lgb
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV, StratifiedKFold
class my_model(object):
    def __init__(self,X,y):
        self.X,self.y = X,y
        self.__lgb_para ={'task': 'train',
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
        self.__iscv = True
        self.__foldnum = 10
    def my_model(self,op = 'gbdt',IS_CV=True,FOLD_NUM=10):
        self.__iscv,self.__foldnum,self.__modelname= IS_CV,FOLD_NUM,op
        if IS_CV:
            splits = list(StratifiedKFold(n_splits = FOLD_NUM,shuffle = True).split(self.X,self.y))
            preds_val = []
            y_val = []
            for idx, (train_idx,val_idx) in enumerate(splits):
                K.clear_session()
                print("Now fold %d"%(idx+1))

                train_X,train_y,val_X,val_y = X[train_idx],y[train_idx],X[val_idx],y[val_idx]
                
                if op == 'gbdt':
                    lgb_train = lgb.Dataset(train_X,train_y,free_raw_data= False)
                    lgb_valid_set = lgb.Dataset(val_X,val_y,reference=lgb_train,free_raw_data = False)
                    gbm =lgb.train(self.__lgb_paras ,
                                   lgb_train,
                                   boost_rount = 2000 #interation num
                                   lgb_valid_set,
                                   early_stopping_round = 20
                                   )
                    #save gbm_model
                    gbm.save_model("gbdt"+"{}".format(idx)+".txt")
    def my_prediction(self,path='',pre_X):
        if self.__iscv:
            for idx in range(self.__foldnum):
                if self.__modelname == 'gbdt':
                    bst = lgb.Booster(path+model_file = self.__modelname+"{}".format(idx+1)+".txt")
                    pred = bst.predict(pre_X,num_iteration=bst.best_iteration)
        return y
