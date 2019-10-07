import numpy as np

### Slicing operation using 2D array ###

#Initializing a 2 dimensional array:
array1 = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print("2D array: ", array1)
#Get a specific element in array[r,c]:(second row six element)
print("Get second row six element:", array1[1,5])
print("Get second row six element:", array1[1,-2])
#Get specific row all elements:
print("Get second row all elements: ", array1[1,:])
#Get specific column all elements:
print("Get second column all elements: ", array1[:, 1])
#Get first row specific element:[startindex:endindex:stepvalue]
print("first row 3, 5 elements: ", array1[1, 2:5:2])
print("first row 3, 5 elements: ", array1[1, 2:-2:2])
#Change perticular element in array(changing scond row 6th element 13 to 20):
array1[1,5] = 20
print("Now array: ",array1)
#Change group value together(change 2nd column all value as 5):
array1[:,2] = 5
print("Now array1", array1)
#Change group value together(change 2nd column valuea are as 1,2):
array1[:,2] =[1,2]
print("Now array1", array1)

#More slicing operations:
arr1 = np.array([[6, 7,8],[1,2,3],[9,3,2]])
#Get 1 and 3 row 's 3th column values:
print("Get 1 and 3 row 's 3th column values: ", arr1[0:3:2, 2])
print("Get 1 and 3 row 's 3th column values: ", arr1[[0,2], 2])
#Get last row 1 and 2 column values:
print("Get last row 1 and 2nd column values: ", arr1[-1, 0:2])





