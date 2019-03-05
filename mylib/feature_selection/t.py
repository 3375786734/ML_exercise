import pandas as pd 
import numpy as np
'''
df = pd.DataFrame(data = [[1,2,3],[4,5,6]],columns=None,index = None)
print(np.mean(df))
print(df.mean())
'''
class hello(object):
    def __init__(self,raw_data):
        self.raw_data = raw_data
        self.__raw_data = raw_data
    def printo(self):
        hhh = 0
        print(self.__raw_data)
