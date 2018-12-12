import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arrange(4)

# NOTE: The following examples will perform elementwise operations
# Arithmetic
a + b  # [20, 31, 42, 53]
a - b  # [20, 29, 38, 47]
a * b  # [0, 30, 80, 150]
b / a  # [0., 0.0333, 0.05, 0.06]
a ** b  # [1, 30, 1600, 125000]
b // a  # [0, 0, 0, 0]

# Logical
a > b  # [True, True, True, True]
a >= b
a < b  # [False, False, False, False]
a <= b
a == b  # [False, False, False, False]
a != b

# Bitwise
a >> 1
b << 2
a & b
a | b
a ^ b
~a

# To perform matrix multiplication use @ (python >= 3.5) or dot function
print(a.dot(b))  # 260
print((a@b) == a.dot(b))  # True

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

print(A.dot(B))

# Operations such as += *= etc can be used
# to modify an existing array instead of creating a new one
a = np.ones(2, 3)
a *= 3
