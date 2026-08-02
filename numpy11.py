
import numpy as np

ar_range = np.arange(5,20)


print(ar_range)
print(ar_range.shape)
print(ar_range.size)

a = np.zeros((2,3), dtype = int)
print("array = ", a)
print("----------------------------------------")
print("dimension = ", a.ndim)
print("----------------------------------------")

print("shape = ", a.shape)

print("----------------------------------------")
print("size = ", a.size)
print("----------------------------------------")

print("Data Type = ", a.dtype)
print("------------------------------------------")

a1 = np.zeros((2,3))
print("data type of {} is {}".format(a1,a1.dtype))    #Float64 # default = float
                                                     # for int:  dtype = int                   

print("\n\n\n")

print("----------------------------------------")
print("----------------------------------------")


a2 = np.ones((1,7), dtype = int)
print("array = ", a2)
print(" dimension = ", a2.ndim)


#full array
print("\n\n\n")

full1 = np.full((5,6),9)
print("\n\n\n")
print("--------------------------")

print(" Full Array = ", full1)

print("data type = ", full1.dtype)


full12 = np.full((5,6),9, dtype=float)

print("dimension of array {} is [{}] and data-type = [{}]".format(full12,full12.ndim,full12.dtype))

# identity matrix

id4x = np.eye(4, dtype=int)

print("-----")

print("Identity matrix = ", id4x)


random1 = np.empty(7)
print("Random Matrix = ", random1)


zz = np.array([4,5,6])
print(zz)

print("\n\n\n")

import numpy as np

# Creating a 2D array (Matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("\n\n\n")

print(matrix)

print("\n\n\n")

print(matrix.ndim)   # Output: 2
print(matrix.shape)  # Output: (2, 3)
print(matrix.dtype)  # Output: int64
print("---------------------------")

print(type(matrix))

print("---------------------------")

"""

import timeit

print(timeit.timeit(
    "np.zeros((1000,1000))",
    setup="import numpy as np",
    number=100
))


""" 

