# Simple Calculator Program which work on python console..
# This program performs basic arithmetic operations like Addition, Subtraction, Multiplication, and Division

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Giving a Error! Division by zero is not allowed."
    return a / b


# Display calculator menu
print("--------Simple Calculator--------")
print("1. For Addition:")
print("2. For Subtraction:")
print("3. For Multiplication:")
print("4. For Division:")
print("5. For Exit from Calculator:")

while True :
    # Taking user input
    choice = input("Enter your choice code which operation you want to perform: ")

    # Perform operation based on user choice
    if (choice == '1'):
        # Input numbers
        num1 = float(input("Enter the first operand: "))
        num2 = float(input("Enter second operand: "))
        print("Your Result of Addition is: ", add(num1, num2))

    elif (choice == '2'):
        # Input numbers
        num1 = float(input("Enter the first operand: "))
        num2 = float(input("Enter second operand: "))
        print("Your Result of Subtraction is: ", subtract(num1, num2))

    elif (choice == '3'):
        # Input numbers
        num1 = float(input("Enter the first operand: "))
        num2 = float(input("Enter second operand: "))
        print("Your Result of Multiplication is: ", multiply(num1, num2))

    elif (choice == '4'):
        # Input numbers
        num1 = float(input("Enter the first operand: "))
        num2 = float(input("Enter second operand: "))
        print("Your Result of Division is: ", divide(num1, num2))

    elif(choice == '5'):
        print("Dhanyawad aaapne humara system use kiya")
        break
     
    else :
        print("You Entered Invalid choice! Please Enter a valid choice Code.")
   
    
