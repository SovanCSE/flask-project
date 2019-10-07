import numpy as np

#Iterate numpy arrays:
arr1 = np.arange(0,15).reshape(3,5)
print("arr1", arr1)
#iterate each row
for row in arr1:
    print("row: ", row)
#Iterate each cell element one by one
for row in arr1:
    for cell in row:
        print("cell: ", cell)
#Another way to iterate cell by cell using single for loop
for cell in arr1.flatten():
    print("Cell : ", cell)

#Use of np.nditer() function
#Iterate each cell element one by one rowwise
for cell in np.nditer(arr1, order='C'):#(default order='C')==> iterate row wise
    print("cell: ", cell)
#Iterate each cell element one by one rowwise
for cell in np.nditer(arr1, order='F'):#(default order='C')==> iterate row wise
    print("cell: ", cell)

#Iterate each row:
for row in np.nditer(arr1,order='C', flags=['external_loop']):
    print("row:", row)
#Iterate each column:
for row in np.nditer(arr1,order='F', flags=['external_loop']):
    print("column:", row)

#Modified array using iteration:
print("original array: ", arr1)
for row in np.nditer(arr1, op_flags=['readwrite']):
    row[...] = row*2
print("After 2 multiplication: ", arr1)
#Iterate two array together
arr2 = np.arange(0,3).reshape(3,1)
print("arr1: ", arr1)
print("arr2: ", arr2)
for cell1, cell2 in np.nditer([arr1, arr2]):#More check general broadcasting rules for multiple array iterate simultaneously
    print("cell1", cell1, " cell2: ", cell2)