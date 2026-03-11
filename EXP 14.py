import numpy as np

# List Operations
print("---------List Operations--------------")
nums = [50, 60, 70, 80, 90, 40, 75]

print("The actual List:", nums)

# Indexing in python
print("\n-----------Indexing Concept------------")
print("First element of the list: ", nums[0])
print("Second element of the list: ", nums[1])
print("Third element of the list: ", nums[2])
print("Last element of the list: ", nums[-1])

# Slicing in python
print("\n------------Slicing Concept------------")
print("The first two elements of the list: ", nums[0:2])
print("The last two elements of the list: ", nums[-2:])
print("The element from index 2 to 5:", nums[2:6])
print("The element from index 3 to last element:", nums[3:])
print("The element from index 4 to last element:", nums[-3:-1])

# Sorting Concept
print("\n-------------Sorting Concept------------")
ascending = sorted(nums)
print("The sorted list in ascending: ", ascending)

descending = sorted(nums, reverse=True)
print("The sorted list in descending: ", descending)

# Matrix Concept
print("\n-------Matrix Operations using Numpy------")
matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2 = np.array([[9,8,7],[6,5,4],[3,2,1]])

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)

# Matrix Addition
add_matrix = np.add(matrix1, matrix2)
print("\nThe Matrix after Addition:\n", add_matrix)

# Matrix Multiplication
mul_matrix = np.dot(matrix1, matrix2)
print("\nThe Matrix after Multiplication:\n", mul_matrix)