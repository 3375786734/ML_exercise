import numpy as np
import pandas as pd
import tqdm as tqdm
'''
We'd better extract feature as matrix data.

@describ: a objec which will extract feature
@para:one onject per raw,if column,please transpose it first.
'''
class feature_extracter(object):
    def __init__(self,raw_data,data_info):
        self.__raw_data = np.transpose(np.array(raw_data))
        self.__data_info = data_info
    def printdata(self):
        print(self.__data_info.info())
        print(self.__raw_data.info())
    def __min_max_regu(self,idata,range_needed = (-1,1)):
        maxv,minv = max(idata),min(idata)
        std_data = (idata - minv)/(maxv-minv)
        return std_data *(range_needed[1]-range_needed[0]) + range_needed[0]

    '''
    @para  : dataframe ,block, range
    @return: np.array ,feature of a single sequence data. 
    @shape : 1*len of feature here we have #19 features
    '''
    def __my_feature_extraction_1(self,idata,block = 160,range_needed = (-1,1)):
        '''
        In this function ,we divivd the sequence into some local pecies
        and extract features including : 
        mean,std,statistical_range(that is mean +- std), percentil,we can change
        this block when case differ.
        '''
        std_data = self.__min_max_regu(idata,range_needed)
        data_len = len(std_data)
        block_size =data_len//block
        feature = []
        for start_point in range(0,data_len,block_size):
            std_data_block = std_data[start_point:start_point+block_size]
            mean = std_data_block.mean()
            std = std_data_block.std()
            std_top,std_bot = mean+std,mean-std
            
            '''
            why those percentil? I don't know
            '''
            percentil_calc = np.percentile(std_data_block,[0,1,25,50,75,99,100])
            
            max_range = percentil_calc[-1] - percentil_calc[0]

            relative_percen = percentil_calc - mean
            '''
            concatenate all the atom feature and 
            '''
            feature.append(np.concatenate([np.asarray([mean,std,std_top,std_bot,max_range]),percentil_calc,relative_percen]))
        return np.asarray(feature)

    '''
    @para  : only __raw_data
    @return:we have 160-time steps feature here,each time step has three phase feature
    @shape : num_of_line * num_of_time_step * (num_feature_pre_line *3)
    '''
    def get_feature_1(self):
        data_len = len(self.__raw_data)
        feature,label,sp = [],[],0
        for id_needed  in tqdm.tqdm(range(sp,data_len+sp,3)):
            tmp = []
            for phase in [0,1,2]:
                now_id = id_needed + phase
                print("now at {} current phase is {} now id is {}".format(id_needed//3,phase,label,now_id))
                if phase == 0:
                    label.append(self.__data_info.loc[now_id].loc['target'])
                    #print("label is {}".format(self.__data_info.loc[now_id].loc['target']))
                #return size = 3*seq_len*feat_per_line
                #print("block shape",self.__raw_data.shape)
                tmp.append(self.__my_feature_extraction_1(self.__raw_data[now_id]))
            #print("tmp size is ",np.array(tmp).shape)
            tmp = np.concatenate(tmp,axis = 1)#return size = seq_len*feat_three_line
            #print("tmp after con",np.array(tmp).shape)
            feature.append(tmp)
            #print("feature size is",np.array(feature).shape)
        return np.asarray(feature),np.asarray(label)
