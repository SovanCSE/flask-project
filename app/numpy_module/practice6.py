import numpy as np

#link==> https://github.com/KeithGalli/NumPy/blob/master/NumPy%20Tutorial.ipynb
#Linear algebra with numpy
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
product_matrix = arr1.dot(arr2)
print("Matrix product between arr1 and arr2 :", product_matrix)