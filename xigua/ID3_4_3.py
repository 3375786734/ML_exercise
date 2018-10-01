from dtreeplot import dtreeplot
import math

#定义树节点
class Node(object):
    def __init__(self,attr_init=None,label_init=None,attr_down_init):
        lself.attr=attr_init
        self.attr_down=attr_down_init
        self.label=label_init
'''
@para label_arr:
@return different_label and it's 
'''
def Nodelabel(label_arr):
    label_count={}



'''
@param df:pandas frame of dataset(data_frame)
@return rt of the decision_tree
'''
def TreeGenerate(df):
    new_node=Node(None,None,{})
    #由于label 在xigua3.0的最后一列,因此使用-1就得到了最后一列
    label_arr=df[df.columns[-1]]
    
    label_count=NodeLabel(label_arr)
    #如果列表中有元素,那么就可以生成decision_tree
    if label_count:


