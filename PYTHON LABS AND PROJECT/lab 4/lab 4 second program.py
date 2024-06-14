def remove_duplicates(string):
    seen = set()
    result = []

    for char in string:
        if char not in seen:
            result.append(char)
            seen.add(char)
        elif char == ' ' or char == '\n':  # Preserve spaces and newlines
            result.append(char)

    return ''.join(result)

# Given input
Input = "String and String Function"

# Remove duplicate characters
output = remove_duplicates(Input)

# Print the output
print("Output:", output)
