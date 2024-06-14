def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Get input from the user
n= int(input("Enter a number: "))

# Call the function to check the number and print the result
print("The number is", check_number(n))
