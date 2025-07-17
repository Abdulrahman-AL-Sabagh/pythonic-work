import numpy as np

# in numpy dimensions are called axes
# [1,2,1] has one axis that has 3 elemns in it
#
# 2 axes will look like this
#  [
#     [1.,0., 0],
#     [1.,0., 0],
#  ]
#
#
arr1 = np.arange(15).reshape(3, 5)

print("Size of the array", arr1.size)
print("Dimension of the array", arr1.ndim)
print("Data of the array", arr1.data)
print("Datatype of the array", arr1.dtype)
print("Shape of the array", arr1.shape)

# Another way to crate a 2D Array
b = np.array([(1, 2, 3), (4, 5, 6)])

# Other methods to crate arrays are .zero(), .ones(), .empty()


# Sequence of numbers would be
# The first paramter is "Start with the number xy", the second number is the end, the third arg is the step
# In this case we are alaways adding by 5
np.arange(10, 30, 5)
# Output would be [10, 15, 20, 25, 30]
# linespace is similar to the range. the only difference is that we set the start and the end and the acount of the elemnts we want to have
# The library will calculate the "Step" by itself
np.linspace(0, 2, 9)

# Operations in numpy

# First of all we have to understand the mathemathical structure we are dealing with

# One dimensional arrays are probably something series. We can add 2 sereis. Subtract their entries from each other. multplicate their entires with each other etc


# Matrix Operations

# 2 types of products
# Elemntwise product {{A_11 * B_11, A_12 * B_12}, {A_21 * B_21}....}

# If we have 2 matrcies A and B then A * B will be the elmentwise product

# A @ B will be the Real matrix Product or A.dot(B)
