def count_characters(string):
    letters = 0
    digits = 0
    symbols = 0

    for char in string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1

    return letters, digits, symbols

# Given input
Input = "P@#yn26at^&i5ve"

# Count letters, digits, and special symbols
letters, digits, symbols = count_characters(Input)

# Print the counts
print("Chars =", letters, "Digits =", digits, "Symbol =", symbols)
