def find_duplicates(lst):
    # Initialize an empty list to store duplicate values
    duplicates = []
    
    # Initialize an empty set to keep track of unique values encountered so far
    seen = set()
    
    # Iterate through the list
    for item in lst:
        # If the item is already in the set, it's a duplicate
        if item in seen:
            duplicates.append(item)
        else:
            # Otherwise, add it to the set
            seen.add(item)
    
    return duplicates

# Sample list
sample_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 8]

# Find and display duplicate values
print("Duplicate values:", find_duplicates(sample_list))
