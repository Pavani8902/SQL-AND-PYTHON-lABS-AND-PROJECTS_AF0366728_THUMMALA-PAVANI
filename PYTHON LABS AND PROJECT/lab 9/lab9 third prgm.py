import numpy as np

# Input inventory data
inventory = np.array([10, 0, 5, 0, 20, 0])

# Find the indices of products that are out of stock
out_of_stock_indices = np.where(inventory == 0)[0]

# Output the indices of out of stock products
print("Out of Stock Products:", out_of_stock_indices)
