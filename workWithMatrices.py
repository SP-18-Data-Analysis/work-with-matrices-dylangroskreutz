# Dylan Groskreutz
# HW Assignment 2 Work with Matrices

import numpy as np

a = np.random.rand(3,3)
print("This is the original matrix produced using random values")
print(a)
print("")

print("Original matrix that has been transposed, reulting in the columns and rows switching")
b = a.T
print(b)
print("")

print("Print out the columns of the matrix one line at a time.")
for row,index in enumerate(b) :
	for col in b[row] :
		print(str(col))
#	print("")

