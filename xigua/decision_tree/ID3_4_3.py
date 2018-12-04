from dtreeplot import dtreeplot
import math

#定义树节点
class Node(object):
    def __init__(self,attr_init=None,label_init=None,attr_down_init):
        self.attr=attr_init
        self.attr_down=attr_down_init
        self.label=label_init

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
        new_node.label = max(label_count,key = label_count.get)
        
        if len(label_count) == 1 or len(label_arr) ==0:
            return new_node
        
        #通过ent获得划分属性,以及div_value
        new_node.attr, div_value = OptAttr(df)

        #离散属性
        if div_value == 0:
            
            value_count = ValueCount(df[new_node.attr])
            for value in value_count:
                df_v = df[df[new_node.attr].isin([value])] 
                df_v = df_v.drop(new_node.attr,1)
                new_node.atrr_down[value] = TreeGenerate(df_v)
        else:   #连续属性
            value_l = "<=%.3f"%div_value
            value_r = ">%.3f"%div_value
            df_v_l = df[df[new_node.attr] <=div_value]
            df_v_r = df[df[new_node.attr] > div_value]
            new_node.attr_down[value_l] = TreeGenerate(df_v_l)
            new_node.attr_down[value_r] = TreeGenerate(df_v_r)
    return new_node


'''
@para label_arr:a array
@return different_label a dictionary with label and count each label as label_count[label]
'''
def Nodelabel(label_arr):
    label_count={}
    for label in label_arr:
        if label in label_count:label_count[label]+=1
        else label_count[label]=1;
    return label_count

def ValueCount(data_arr):
    value_count  = {}
    for label in data_arr:
        if label in value_count:value_count[label] +=1
        else : value_count[label] =1
    return value_count

'''
@para data_frame
@return optimal_attribute and it's value
'''
def OptAttr(df):
    info_gain=0


    #visit all col except the last one since it is the label:
    for attr_id in df.columns[1:-1]:
        #calculate the imformation gain of the current attr_id
        info_gain_tmp,div_value_tmp=InfoGain(df,attr_id)
        #find the one with the maximum imformation gain
        if info_gain_tmp>info_gain:
            info_gain=info_gain_tmp
            div_value=div_value_tmp
            opt_attr=attr_id
    return opt_attr,div_value


def InfoGain(df,index):
    info_gain = InfoEnt(df.value[:,-1])
    div_value = 0

    n = len(df[index])

    if df[index].dtype ==(float ,int):
        sub_info_ent = {}
        
        df = df.sort([index].accending = 1)
        df = df.reset_index(drop = true)
        
        data_arr = df[index]
        label_arr = df[df.columns[-1]]
        

        for i in range(n-1):
           div_value = 
    else :  #离散属性
        data_arr = df[index]
        label_arr = df[df.columns[-1]]
        value_count = ValueCount(data_arr)

        for key in value_count:
            key_label_arr = label_arr[data_arr == key]
            info_gain -= value_count[key]*InfoEnt(key_label_arr) 
    return info_gain,div_value


if __name__=='__main__':

