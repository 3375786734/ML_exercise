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
    for label in label_arr:
        if label in label_count:label_count[label]+=1
        else label_count[label]=1;


'''
@para
@return 
'''
def InfoEnt(label_arr):
    Ent=0
    N=len(label_arr)
    label_count
    for label in label_arr:
        Ent-=(label_count)
    

'''
@para
@return 
'''
def InfoGain(df,index):
    info_gain=InfoEnt(df.value[:,-1])
    div_value=0




'''
@para data_frame
@return optimal_attribute and it's value
'''
def OptAttribute(df):
    info_gain=0

    for attr_id in df.columns[1:-1]:
        info_gain_tmp,div_value_tmp=InfoGain(df,attr_id)
        if info_gain_tmp>info_gain:
            info_gain=info_gain_tmp
            div_value=div_value_tmp
            opt_attr=attr_id
    return opt_attr,div_value



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
   




if __name__=='__main__':

