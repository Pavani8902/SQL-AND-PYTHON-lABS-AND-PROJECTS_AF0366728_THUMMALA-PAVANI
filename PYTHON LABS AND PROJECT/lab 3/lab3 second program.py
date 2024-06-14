def remove_newline(string):
    # Replace newline characters with an empty string
    string_without_newline = string.replace("\n", "")
    return string_without_newline

# Given string
Python_String = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters from the given string
modified_string = remove_newline(Python_String)

# Print the modified string
print("Modified String:", modified_string)
