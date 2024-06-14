import numpy as np

# Input data
quantity = np.array([2, 3, 4, 1])
price_per_item = np.array([10.0, 5.0, 8.0, 12.0])

# Calculate the total cost of each item
total_cost_per_item = quantity * price_per_item

# Output the total cost of items
print("Total Cost of Items:", total_cost_per_item)
