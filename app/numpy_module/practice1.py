import numpy as np

#Creating 1D array
array1 = np.array([1,2,3,4])
print("1D array: ", array1)
#Createing 2D array using numpy
array2 = np.array([(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)])
print("2D array: ",array2)
#Get dimensions:
print("No of dimensions of the array1: ", array1.ndim)
print("No of dimensions of the array2: ", array2.ndim)
#Get Shape
print('Shape of the array1: ', array1.shape)
print('Shape of the array2: ', array2.shape)
#Get each item size
print('Each element size of the array1: ', array1.itemsize)
print('Each element size of the array2: ', array2.itemsize)
#Get no of elements
print("Total no of element in array1: ", array1.size)
print("Total no of element in array2: ", array2.size)
#Get size of array
print("Total size of array1: ", array1.nbytes)
print("Total size of array1: ", (array1.size*array1.itemsize))
print("Total size of array2: ", array2.nbytes)
print("Total size of array2: ", (array2.size*array2.itemsize))
#Datatype of the array
print("Datatype of the array1: ", array1.dtype)
print("Datatype of the array2: ", array2.dtype)
#change datatype of array:
array3= np.array([1,2,3,4], dtype='float16')
print("array3: ", array3)

#Use of arange function
arr1 = np.arange(1,6)
print("arr1: ", arr1)
arr1 = np.arange(1,10,2)
print("arr1", arr1)

#Use of linspace function
#If you want to get 5 number between 1,10
arr2 = np.linspace(1,10,5).astype(dtype=np.int16)
print('arr2',arr2)



