# simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

def calculator():
    num1 = float(input("Enter first number: "))
    operation = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number:"))
    
    if 