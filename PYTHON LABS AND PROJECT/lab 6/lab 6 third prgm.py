def split_list(lst, length_first_part):
    # Check if the given length is valid
    if length_first_part >= len(lst):
        return "Error: Length of the first part exceeds or is equal to the length of the list."
    
    # Split the list into two parts
    first_part = lst[:length_first_part]
    second_part = lst[length_first_part:]
    
    return (first_part, second_part)

# Original list
original_list = [1, 1, 2, 3, 4, 4, 5, 1]

# Length of the first part of the list
length_first_part = 3

# Split the list into two parts
result = split_list(original_list, length_first_part)

# Print the result
print("Original list:", original_list)
print("Length of the first part of the list:", length_first_part)
print("Splitted the list into two parts:", result)
