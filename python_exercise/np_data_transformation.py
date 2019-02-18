import numpy as np

#################################################################
#           how to select some element in np                    #
#################################################################

a = np.array([1,2,3,4,5,6])


#select data from i-th column to j-th column [i:j+1] ,starting from 0-column
print(a[1:2])
print(a[0:-1])

#treat b as index ,select all the element in c which have the index as b
b = [0,2,3]
c = []
c = a[b]
print(c)


