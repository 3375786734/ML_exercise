import pandas as pd
import numpy as np
import os
import platform
import pyarrow.parquet as pq

class io_py(object):
    def __init__(self):
        data = []

    def __get_suffix(path):
        suf_pos = -1
        p_len = len(path)
        while path[suf_pos]!='.':
            suf_pos--
        suffix = suffix[suf_pos+1:p_len]
        return suffix

    def read_data(path,op):
        suffix = __get_suffix(path)
        if suffix=="csv" :
            return __csv2pd(path) if op=="pd" else np.array(__csv2pd(path))
        elif suffix == "parquet":
            return __parquet2pd(path) is op=="pd" else np.array(__parquet2pd(path))

    def __csv2pd(path):
        try:
            return pd.read_csv(path)
        except:
            print("Can't find"+ path)
            return pd.DataFrame(None)
    
    def __parquet2pd(path):
        try:
            return pq.read_pandas(path).to_pandas()
        except:
            print("Can't find"+path)
            return pd.DataFrame(None)
