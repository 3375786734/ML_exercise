import numpy as np
import pandas as pd
'''
tmp=list(range(2,5))
st=",".join([str(i) for i in tmp])
with open('test.csv','r+') as f:
    content=f.read()
    f.seek(0,0)
    f.write(st+"\n"+content)
'''
data=pd.read_csv('test.csv')
#x=np.array(list(data[]))
#y=np.array(list(data[:2]))
cols= data.columns
cnt=0
x=np.array([list(data['2'])])
#print(x)
for i in cols[1:]:
    x=np.r_[x,np.array([list(data[i])])]
print(x)
