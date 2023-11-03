"""
The greatest common divisor of two positive integers A and B is the largest number that can be evenly divided into both of them.
Euclid's algorithm can be used to find the greatest common divisor (GCD). The algorithm is as follows:
- Compute remainder of large number divided by small number
- Replace large number with the small number and the small number with the remainder
- Repeat until the smaller number is 0
- At this point the larger number is the GCD

Write a program that lets a user input two positive integers and returns the GCD.
"""
largeNumber = int(input('Enter larger number: '))
smallNumber = int(input('Enter smaller number: '))

#print(largeNumber % smallNumber)

while(smallNumber != 0):
    remainder = largeNumber % smallNumber
    largeNumber = smallNumber
    smallNumber = remainder

print('GCD is', largeNumber)