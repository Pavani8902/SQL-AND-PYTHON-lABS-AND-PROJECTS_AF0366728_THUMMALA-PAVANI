def reverse_words(string):
    # Split the string into words
    words = string.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Join the reversed words back into a string
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

# Given string
String = "Deeptech Python Training"

# Reverse the words in the given string
reversed_string = reverse_words(String)

# Print the reversed string
print("Reversed String:", reversed_string)
