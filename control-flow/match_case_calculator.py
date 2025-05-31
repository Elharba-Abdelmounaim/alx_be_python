# match_case_calculator.py

# Prompt the user to enter the first number and convert it to float
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number and convert it to float
num2 = float(input("Enter the second number: "))

# Ask the user to choose an arithmetic operation
operation = input("Choose the operation (+, -, *, /): ")

# Use match-case to handle the selected operation
match operation:
    case "+":  # Addition
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":  # Subtraction
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":  # Multiplication
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":  # Division
        if num2 == 0:
            # Handle division by zero
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:  # Handle invalid operation input
        print("Invalid operation.")

