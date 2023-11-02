"""
Write a program that takes a sphere's radius as input and returns its diameter, circumference, surface area and volume as outputs
"""
radius = float(input("Enter the sphere's radius: "))
diameter = radius * 2
approxPi = 3.14
circumference = approxPi * diameter
surfaceArea = 4 * approxPi * radius ** 2
volume = (4/3) * approxPi * radius ** 3

print("Diameter = " + str(diameter))
print("Circumference = " + str(circumference))
print("Surface Area = " + str(surfaceArea))
print("Volume = " + str(volume))