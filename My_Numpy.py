import numpy as np

#1 D array
n1=np.array([1,2,3])
n1

#2 D array
n2=np.array([["jajja","ajajja"],[3,5]])
print(n2)

n1.shape
#shape of column

#type of dimention
n1.dtype
n2.dtype

#number of dimention
n2.ndim


#array craetion method

#Zeros Numpy
np.zeros((2,3))  #Using tuple
np.zeros([2,3])  #Using List

#Ones Array
np.ones((2,3))

#Identity matrix
np.eye(3)
#There will be only one input


#arange matrix
np.arange(1,10)
np.arange(1,10,2)
np.arange(0,10,2)


#linspace->(1 theke 2 porjonto 5 ta value)
np.linspace(1,2,5)
np.linspace(1,2,1)