"""
A tax calculator program outputs a floating point number with more than two digits of precision.
Use the round function to modify the program to display two digits of precision.
"""
prompt = 'Enter a number: '
num = float(input(prompt))
print(round(num, 2))