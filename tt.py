import pandas as pd
import numpy as np
a = list([[1,2,3],[4,5,6]])
df = pd.DataFrame(a)
print(df.loc[0])
print(a[1])
data = np.random.rand(500, 10)
label = np.random.randint(2, size=500)
print(data)
print(label)
