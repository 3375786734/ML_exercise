'''
del function will clean up variables instead of value.

In ML/DM tasks ,del variable before loading the data is always a good habit.

see deatail in CS231N - KNN.ipynb
'''
a = 1
b = a
c = a
del a
del b
print(c)
