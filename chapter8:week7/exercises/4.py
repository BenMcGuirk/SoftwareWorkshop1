"""
Write a Python program that acts as a simple calculator. The program should ask the user for two numbers and an operation 
(addition, subtraction, multiplication, or division). Use try-except blocks to handle any exceptions that might occur, such 
as ZeroDivisionError (when the user tries to divide by zero) or ValueError (when the user inputs something that's not a number).
"""
try:
    int1 = int(input("Enter the first number: "))
    int2 = int(input("Enter the second integer: "))
    sign = input("Enter the operation (+, -, / or *): ")
except ValueError:
    print('Please enter a valid number')

def Addition(int1, int2):
    print(int1 + int2)

def Subtraction(int1, int2):
    print(int1-int2)

def Division(int1, int2):
    try:
        print(int1/int2)
    except ZeroDivisionError:
        print('Cannot divide by zero.')

def Multiplication(int1, int2):
    print(int1 * int2)

if sign == '+':
    Addition(int1, int2)
elif sign == '-':
    Subtraction(int1, int2)
elif sign == '/':
    Division(int1, int2)
elif sign == '*':
    Multiplication(int1, int2)