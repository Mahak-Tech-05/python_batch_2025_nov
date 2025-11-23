#numpy command:-pip install numpy
import numpy as np

#creating a 1d array
arr1 = np.array([10,20,30,40])
print("1d array numpy:", arr1)

# creating a 2d array (matrix)
arr2 = np.array( [
[1,2,3],
[4,5,6]
    ] )
print("2d arry:\n:", arr2)

#basic operations
print("Adding each element with 10:", arr1 + 40)
print("Adding each element wiht 10:" , arr2+10)
print("-----------------------------------")
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
for i in range(len(matrix)):#row index
    for j in range(len(matrix[i])):#column index
                   matrix[i][j] = matrix[i][j] +10

print(matrix)
