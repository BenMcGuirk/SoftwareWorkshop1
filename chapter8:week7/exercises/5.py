"""
You have a dictionary of student names and their corresponding grades. Write a function that takes a student's name as 
input and returns their grade. If the student's name is not found in the dictionary, handle the exception and inform the user.
"""

grades = {
    'Finn' : 89,
    'Abi' : 91,
    'Carlos' : 24,
    'Ben' : 99
}

try:
    name = input("Enter your name: ")
    print(grades[name])
except KeyError:
    print(f'Sorry there is no grade for {name}')
