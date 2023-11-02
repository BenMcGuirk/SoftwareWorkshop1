"""
Write a program that accepts the lengths of three sides of a triangle as inputs. Output whether or not the triangle is an 
equilateral.
"""

side1 = input("Enter the length of side 1: ")
side2 = input("Enter the length of side 2: ")
side3 = input("Enter the length of side 3: ")

if side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is an equilateral")
else:
    print("The trianlge is not an equilateral")