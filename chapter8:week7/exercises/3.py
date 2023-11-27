"""
Create a function that asks the user to input their birth year and calculates their age. If the user enters an invalid 
value that cannot be converted to an integer, handle the exception by asking the user to input a valid year.
"""

try:
    year = int(input("Enter your birth year: "))
    age = 2023 - year
    print('Your are', age, 'years old!')
except:
    print("Please enter a valid integer")