def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

# Example usage
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

divide_numbers(numerator, denominator)
