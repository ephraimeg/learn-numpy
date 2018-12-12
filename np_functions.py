import numpy as np

a = np.arange(3)
b = np.arange(15).reshape(3, 5)

# Questions
np.all(a)  # tests wether all array elements evaluate to True
np.any(a)  # checks whether an element evaluates to True

# Ordering
# NOTE calling np.sort(a) is different from calling a.sort()

np.min(a)  # returns value of min element in the matrix
np.max(a)  # returns value of max element in the matrix
np.sort(a)  # returns a sorted copy of the matrix
np.argmax(a)  # returns indices of max elements in the matrix
np.argmin(a)  # returns indices of min elements in the matrix

# Operations
np.sum(a)  # returns the sum of the elements in the matrix
np.comsum(a)  # returns a matrix whose elements are a cumulative sum of mat A
np.prod(a)
np.cumprod(a)

# Statistics
np.std(a)  # returns a new array containing the standard deviation
np.mean(a)  # returns arithmetic mean of the matrix
np.median(a)  # returns median of the matrix
