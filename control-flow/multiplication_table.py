# multiplication_table.py

# Ask the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    # Calculate the product of the user's number and the current number in the loop
    result = number * i

    # Print the multiplication line in the format: X * Y = Z
    print(f"{number} * {i} = {result}")

