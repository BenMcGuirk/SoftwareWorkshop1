"""
Write a program that accepts three sides of a triangle as input. The program should indicate whether or not the triangle is a
right angle. Recall from pythagorean theorem that in a right angle triangle, the square of one side equals the sum of the squares
of the other sides (A^2 + B^2 = C^2).
"""
a = int(input("Enter length a: "))
b = int(input("Enter length b: "))
c = int(input("Enter length c: "))

if a**2 + b**2 == c**2:
    print("Triangle is a right angle")
elif b**2 + c**2 == a**2:
    print("Triangle is a right angle")
elif a**2 + c**2 == b**2:
    print("Triangle is a right angle")
else:
    print("Triangle is not a right angle")

#if all three sides input as 0, it returns that it is a right angle so would need to add quick if statement to remove 0 entry