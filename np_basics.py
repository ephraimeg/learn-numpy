import numpy as np


# create an array with 3 rows and 5 columns with 15 elements (0 - 14)
a = np.arrange(15).reshape(3, 5)
print(a)

# array([[ 0,  1,  2,  3,  4],
#		 [ 5,  6,  7,  8,  9],
#		 [10, 11, 12, 13, 14]])

# try : a = np.arrange(14).reshape(3, 5)
# returns ValueError: cannot reshape array of size 14 into shape (3, 5)

# dimensions of the array: matrix with n rows and m columns has shape (n, m)
print(a.shape)

# number of axes (dimensions) of the array
print(a.ndim)

# dtype - object describing the type of elements in the array
print(a.dtype.name)

# size in bytes of each element of the array
print(a.itemsize)

# total number of elements in the array
print(a.size)
print(type(a))

# transposed copy of the array
print(a.T)

b = np.array([6, 7, 8])
print(b)
print(type(b))

# Ways to create ndarray
a = np.array([2, 3, 4])  # 1D array
b = np.array([(1.5, 2, 3), (4, 5, 6)])  # 2D array
c = np.array([[1, 2], [3, 4]], dtype=complex)  # 2D array with specified type
d = np.zeros((3, 4))  # 2D array initialized with 0s
e = np.ones((2, 3, 4), dtype=np.int16)  # 3D array initialized with 1s
f = np.empty((2, 3))  # 2D array without initialization dtype is 'float64'
g = np.arange(10, 30, 5)  # 1D int array from 10 to 30 with a 5 step
h = np.arange(0, 2, 0.3)  # 1D float array from 0 to 2 with a 0.3 step
i = np.linspace(0, 2, 9)  # 1D float array with 9 elements from 0 to 2
j = np.eye(4)  # identity matrix (4,4)

# additional printing tips
# the last axis is printed from left to right,
# the second-to-last is printed from top to bottom,
# he rest are also printed from top to bottom,
# with each slice separated from the next by an empty line.

np.append(a, b)  # append a with b
np.insert(a, 0, 2, 0)  # insert item 2 at index 0 in array a at axis 0
b.resize((6, 2))  # resize matrix b from (2,6) to (6,2)
# NOTE: resize is different from reshape
np.delete(a, 2)  # deletes item at index 2 from array a
