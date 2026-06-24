# Simple Calculator Program

# Display available operations
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

# Taking operation choice from user
operation = int(input("Enter operation number: "))

# Taking numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


# Checking which operation user selected
if operation == 1:
    # Addition
    print("Answer =", num1 + num2)

elif operation == 2:
    # Subtraction
    print("Answer =", num1 - num2)

elif operation == 3:
    # Multiplication
    print("Answer =", num1 * num2)

elif operation == 4:
    # Division with zero check
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Answer =", num1 / num2)

else:
    # If user enters wrong option
    print("Invalid Operation!")
