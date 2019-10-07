import numpy as np

#Different between shallow and deep copy

#Shallow copy
arr1 = np.array([1,2,3])
arr2 = arr1
arr2[0] = 100
print("arr1", arr1)
print("arr2", arr2)
#Deepcopy
arr1 = np.array([1,2,3])
arr2 = arr1.copy()
arr2[0] = 100
print("arr1", arr1)
print("arr2", arr2)
