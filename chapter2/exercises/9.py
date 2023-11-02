"""
Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles.

- A kilometer represents 1/10,000 of the distance between the North Pole and the equator.
- There are 90 degrees, containing 60 minutes of arc each, between the North Pole and the equator.
- A nautical mile is 1 minute of arc.
"""

kilometers = int(input("Enter the number of kilometers: "))
nauticalMiles = kilometers * 0.54

print("Nautical miles = " + str(nauticalMiles))