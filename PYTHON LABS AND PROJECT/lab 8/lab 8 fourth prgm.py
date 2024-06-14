import numpy as np

# Input list
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# Input tuple
my_tuple = ([8, 4, 6], [1, 2, 3])

# Convert list to array
array_from_list = np.array(my_list)

# Convert tuple to array
array_from_tuple = np.array(my_tuple)

print("Array from list:")
print(array_from_list)

print("\nArray from tuple:")
print(array_from_tuple)
