import math

print("Welcome to the PYhton Calculator")
print("Select an operation to Perform")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. square root (SQROT)")
print("6. raise to power (RSP)")

# sqrtt = math.sqrt(num1)
# raise2 = math.power(num1, num2)

# Prompt the user for the operation they want to perform
def calc():

    
    operation = input("Enter the operation (+,-,*,/,SQROT,RSP): ")

    # Prompt for the numbers

    num1 = input("Enter the first Number: ")
    num2 = input("Enter the second Number: ")

    # Ensure the operation is valid

    if operation not in ['+','-', '*', '/','SQROT', 'RSP']:

        print("Invalid operation. Please try again.")
        return


    # Validate that the numbers are numerical

    try: 
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid numbers: Please enter numeric values.")
        return

    # Validate that the numbers are numerical

    if operation == '/' and num2 == 0:
        print("Error; Division by zero is not allowed.")
        return

    # Use conditional statements to perform the selected operation:

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == 'SQROT':
        result = math.sqrt(num1)
    elif operation == 'RSP':
        result = math.pow(num1, num2)

    print(f'The result of the operation is: {result}')

calc()