import  numpy as np

### Slicing operation using 3D array ###


#Initializing 3D array:
array1 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("3D array: ", array1)
#Get first matrix second row second element inside of 3D array:
print("first matrix second row  at second element:", array1[0,1,1])
#Get second row of each matrix:
print("Get second rows of each matrix in 3d array: ", array1[:,1,:])
#Replace first and second metrix sconds rows are with [8,8] and [9,9]
array1[:, 1, :] = [[8,8], [9,9]]
print("Replace second row of both matrix:",array1)
