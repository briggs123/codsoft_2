def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculator():
    # Prompt user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Dictionary mapping operations to functions
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    # Prompt user to enter an operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation and get the result
    if operation in operations:
        result = operations[operation](num1, num2)
    else:
        result = "Invalid operation"

    # Display the result
    print(f"The result is: {result}")

# Run the calculator function
calculator()
