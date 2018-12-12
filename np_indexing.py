import numpy as np


# Given array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
a = np.arange(10, 101, 10)
index = np.array([0, 0, 2, 4, 4, 1, 5, 3])
print(a[2])  # 30
print(a[index])  # [10, 10, 30, 50, 50, 20, 60, 40]
print(a[2:5])  # [30, 40, 50]
print(a[::2])  # from start to end steps by 2
# [10, 30, 50, 70, 90]

a = np.arange(50).reshape(5, 10)
print(a[1, 1])  # 11 (element on second row, second column)
print(a[0:2])  # all elements in first and second row
print(a[:, 0:2])  # all elements in first and second column
print(a[::2, ::3])
# from first to last row, step by 2
# from first to last column step by 3
# array([[ 0,  3,  6,  9],
#        [20, 23, 26, 29],
#        [40, 43, 46, 49]])
