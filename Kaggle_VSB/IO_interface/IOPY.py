import pandas as pd
import numpy as np
import os
import platform

class io_py(object):
    def __init__(self):
        data = []

    def __get_suffix(self,path):
        suf_pos = -1
        p_len = len(path)
        while path[suf_pos]!='.':
            suf_pos = suf_pos -1
        suffix = path[suf_pos+1:p_len]
        return suffix

    def read_data(self,path,op):
        print("here")
        suffix = self.__get_suffix(path)
        if suffix=="csv" :
            return (self.__csv2pd(path) if op=="pd" else np.array(self.__csv2pd(path)))
        elif suffix == "parquet":
            return (self.__parquet2pd(path) if op=="pd" else np.array(self.__parquet2pd(path)))

    def __csv2pd(self,path):
        try:
            return pd.read_csv(path)
        except:
            print("Can't find"+ path)
            return pd.DataFrame(None)
    
    def __parquet2pd(self,path):
        try:
            return pq.read_pandas(path).to_pandas()
        except:
            print("Can't find"+path)
            return pd.DataFrame(None)
