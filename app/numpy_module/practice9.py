import numpy as np

#Reorganizing array using numpy
#Use of reshape function
arr1 = np.array([[1,2],[4,5],[7,8]])
print("arr1: ", arr1)
print("arr1 shape: ", arr1.shape)
arr2 = arr1.reshape(2,3)
print("arr2 shape: ", arr2.shape)
print("arr2: ", arr2)

#Use of ravel function
#It's basically convert n dimensional array to 1 dimensional array:
arr3 = arr1.ravel()
print("arr3 : ",arr3)

#Use of vstack and hstack function:
arr1 = np.arange(6).reshape(2,3)
arr2 = np.arange(6,12).reshape(2,3)
print("arr1: ", arr1)
print("arr2: ", arr2)
print("Vstack result: ", np.vstack( (arr1,arr2) ))
print("Hstack result: ", np.hstack( (arr1,arr2) ))

#Use of hsplit and vsplit function:
arr1 = np.arange(30).reshape(2,15)
print("arr1: ", arr1)
result = np.hsplit(arr1, 3)
print("hsplit1 ", result[0])
print("hsplit2 ", result[1])
print("hsplit3 ", result[2])
result = np.vsplit(arr1, 2)
print("vsplit1 ", result[0])
print("vsplit2 ", result[1])

#Boolean representation using numpy array:
arr1 = np.arange(12).reshape(3,4)
print("arr1", arr1)
#Get Boolean representation matrix
bool_matric  = arr1>4
print("Boolean matrix: ", bool_matric)
#Get all values which are greater than 4
bool_filter_matrix = arr1[bool_matric]
print("Filtered matrix: ", bool_filter_matrix)
#Replace every value which are greater than 4 with -1
arr1[bool_matric] = -1
print("Replace filter with -1: ", arr1)
