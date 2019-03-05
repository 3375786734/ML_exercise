import IO_interface.IOPY as iopy
import seq_feature
import numpy as np
oi = iopy.io_py()
data_i,data_t = "metadata_train.csv","sample.csv"
datai,datat = oi.read_data(data_i,"pd"),oi.read_data(data_t,"pd")
t_len = len(datai)
n_num = sum(datai['target'])
p_num = t_len - n_num
'''
print("we have total {}/{}data,negative of :{}/{}, positive of {}/{}".format(t_len//3,t_len,n_num,n_num//3,p_num//3,p_num))
'''

'''
print(datai.info())
print(datai.index)
datai = datai.set_index(['id_measurement','phase'])
#这里取了index中levels[0]不同的即,一共有8712个数据,其中 8712/3 根不同线路,因此只有8712/3个index
print(np.array(datai.index.levels[0].unique()).shape)
'''
ext = seq_feature.feature_extracter(datat,datai)
X,y = ext.get_feature_1()
print("X shape",X.shape)
print("y shape",y.shape)
oi.write_data('feature.csv',X,'csv')
