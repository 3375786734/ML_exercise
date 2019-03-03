import numpy as np
import pandas as pd

'''
We'd better extract feature as matrix data.
'''
class seq_feature(object):
    def __init__(self):
        __raw_data = self

    def basic_feature(self,):
        

    def __min_max_regu(self,range_needed = (-1,1)):
        maxv,minv = max(self.__raw_data),min(self.__raw_data)
        std_data = (self.__raw_data - minv)/(maxv-minv)
        return std_data *(range_needed[1]-range_needed[0]) + range_needed[0]
    
    '''
    @para  : 
    @return: np.array ,feature of a single sequence. 
    @shape : 1*len of feature here we have #19 features
    '''
    def __my_feature_extraction_1(self,idata,block = 160,range_needed = (-1,1)):
        '''
        In this function ,we divivd the sequence into some local pecies
        and extract features including : 
        mean,std,statistical_range(that is mean +- std), percentil,we can change
        this block when case differ.
        '''
        std_data = self.__min_max_regu(range_needed)
        data_len = len(std_data)
        block_size = data_len//block
        
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
    @para  :
    @return:we have 160-time steps feature here,each time step has three phase feature
    @shape : num_of_line * num_of_time_step * (num_feature_pre_line *3)
    '''
    def get_feature_1(self):
        data_len = len(self.__raw_data)
        truncate_num = 2
        truncate_size = data_len/truncate_num
        feature,label = [],[]
        '''
        To avoid RAM exceeded ,we truncate the whole dataset into two parts.
        '''
        for sp in range(0,data_len,truncate_size):
            raw_block = self.__raw_data[sp:truncate_size+sp]
            for id_measurement in tqdm():

        feature = np.concatenate(feature)
        feature = np.concatenate(feature)
        return feature,label
     
