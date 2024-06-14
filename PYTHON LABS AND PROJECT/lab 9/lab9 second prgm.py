import numpy as np

# Create a 1D array with values ranging from 2 to 10
values = np.arange(2, 11)

# Reshape the 1D array into a 3x3 matrix
matrix_3x3 = values.reshape(3, 3)

print(matrix_3x3)
