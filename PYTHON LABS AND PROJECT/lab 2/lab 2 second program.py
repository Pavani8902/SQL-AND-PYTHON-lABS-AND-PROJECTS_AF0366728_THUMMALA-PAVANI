def factorial(n):
    # Initialize the factorial result to 1
    result = 1
    
    # Iterate from 1 to n and multiply each number to the result
    for i in range(1, n + 1):
        result *= i
    
    return result

# Ask the user to input a number
number = int(input("Enter a number: "))

# Calculate the factorial using the function
result = factorial(number)

# Print the result
print("The factorial of", number, "is:", result)
