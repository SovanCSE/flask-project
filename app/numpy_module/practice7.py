import numpy as np

#Statistics with numpy
#Use of min, max or sum function
arr1 = np.array([[2,6,8],[1,3,7]])
print("arr1: ", arr1)
#Max value from all element
max1 = arr1.max()
max2 = np.max(arr1)
print("Max1:", max1)
print("Max2: ", max2)
#Max value by row wise comparison
max1 = arr1.max(axis=1)
max2 = np.max(arr1, axis=1)
print("X axis wise max: ", max1)
print("X axis wise max: ", max2)
#Max value by column wise comparison
max1 = arr1.max(axis=0)
max2 = np.max(arr1, axis=0)
print("Y axis wise max: ", max1)
print("Y axis wise max: ", max2)
#Min value from all element
min1 = arr1.min()
min2 = np.min(arr1)
print("Min1: ", min1)
print("Min2", min2)
#Min value by row wise comparison
min1 = arr1.min(axis=1)
min2 = np.min(arr1, axis=1)
print("X axis wise min: ", min2)
print("X axis wise min: ", min2)
#Min value by column wise comparison
min1 = arr1.min(axis=0)
min2 = np.min(arr1, axis=0)
print("Y axis wise min: ", min2)
print("Y axis wise min: ", min2)
#Sum value from all element
sum1 = arr1.sum()
sum2 = np.sum(arr1)
print("Sum1: ", sum1)
print("Sum2: ", sum2)
#Sum value by row wise comparison
sum1 = arr1.sum(axis=1)
sum2 = np.sum(arr1, axis=1)
print("X axis wise sum: ", sum1)
print("X axis wise sum: ", sum2)
#Sum value by column wise comparison
sum1 = arr1.sum(axis=0)
sum2 = np.sum(arr1, axis=0)
print("Y axis wise sum: ", sum1)
print("Y axis wise sum: ", sum2)

#Use of sqrt function
arr2 = np.sqrt(arr1)
print("Square root of arr1: ", arr2)

#Use of std function:
arr3= np.std(arr1)
print("standard deviation value of array1: ", arr3)
