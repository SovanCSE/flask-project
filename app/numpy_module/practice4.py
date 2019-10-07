import numpy as np

### 0s,1s, identical matrixes

#Initialize all zero's(0s) matrix which default dtype='float64':
zero_matrix = np.zeros((2,2))
print("Get 2d 0s matrix", zero_matrix)
#Initialize all zero's(0s) matrix which default dtype='float64':
one_matrix = np.ones((2,2))
print("Get 2d 1s matrix", one_matrix)
#Initialize all elements by other value(datatype depend of value):
other_matrix = np.full((2,2), 55)
print("Get 2d matrix with other value", other_matrix)
#Initialize all elements by other value(datatype depend of value):
otherlike_matrix = np.full_like((2,3), 4, dtype='float16')
print("Get 2d matrix with other value", otherlike_matrix)
#Initializing random number
random1 = np.random.rand(2,3)
print("random1", random1)
#Initializing integer random number with 3, 7 range
random2 = np.random.randint(3,7,size=(3,3))
print("random2", random2)
#Initialize random array with take size from another matrix
random3 = np.random.random_sample(other_matrix.shape)
print("random3: ", random3)
#Get Identity matrix:
iden1 = np.identity(4, dtype='int8')
print("Identity array", iden1)
#Repeat array on 1d :
arr1 = np.array([1,2,3])
repeat_array = np.repeat(arr1,3, axis=0)
print("repeat array: ", repeat_array)
#Repeat array on 2d :
arr1 = np.array([[1,2,3]])
repeat_array1 = np.repeat(arr1,3, axis=0)
print("repeat array on x and y axis: ", repeat_array1)
repeat_array2 = np.repeat(arr1,3, axis=1)
print("repeat array on x axis: ", repeat_array2)




