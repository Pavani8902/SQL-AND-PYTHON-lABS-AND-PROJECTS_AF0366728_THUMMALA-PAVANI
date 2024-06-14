def get_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Error: Please enter a valid integer.")

# Example usage
try:
    user_integer = get_integer_input("Please enter an integer: ")
    print("You entered:", user_integer)
except ValueError:
    print("An error occurred while getting the integer input.")
