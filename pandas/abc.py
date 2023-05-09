import numpy as np 
from scipy import stats
# data=np.array([[10,21,23],[70,23,34],[40,70,20]])
# print(data)
# print(np.mean(data,axis=0))
# print(np.median(data,axis=0))
data=[1,2,3,4,5,67,8]
x=stats.mode(data)
print(x)
