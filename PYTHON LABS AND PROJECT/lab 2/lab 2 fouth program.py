# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Generate Fibonacci numbers up to 50 using a while loop
fib_sequence = [a, b]
while True:
    a, b = b, a + b  # Update Fibonacci numbers
    if b > 50:
        break
    fib_sequence.append(b)  # Add b to fib_sequence

# Print the Fibonacci series
print("Fibonacci series between 0 and 50:")
print(fib_sequence)
