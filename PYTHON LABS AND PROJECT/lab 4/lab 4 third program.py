def count_characters(string):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    return upper_count, lower_count, digit_count, special_count

# Given input
Input = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# Count uppercase, lowercase, numeric, and special characters
upper, lower, digits, special = count_characters(Input)

# Print the counts
print("UpperCase:", upper)
print("LowerCase:", lower)
print("NumberCase:", digits)
print("SpecialCase:", special)
