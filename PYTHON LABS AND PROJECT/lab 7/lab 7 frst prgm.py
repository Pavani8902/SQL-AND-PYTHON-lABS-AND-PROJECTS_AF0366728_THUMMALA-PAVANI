def calculate_mean(dictionary):
    # Calculate the sum of all values
    total_sum = sum(dictionary.values())
    
    # Calculate the mean
    mean = total_sum / len(dictionary)
    
    return mean

# Given dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate the mean
mean = calculate_mean(test_dict)

# Print the mean
print("Mean:", mean)
