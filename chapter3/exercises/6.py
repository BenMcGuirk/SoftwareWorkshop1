"""
The german mathematician Gottfried Leibniz developed the following method to approximate the value of Pi:
Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9...

Write a program that allows the user to specify the number of iterations used for the approximation and display the value.
"""

iterations = int(input("Enter the number of iterations of precision you would like: "))
quarterPi = 1
count = 2
topFrac = 1
bottomFrac = 3

for x in range(iterations):
    if count % 2 == 0:
        quarterPi = quarterPi - (topFrac/bottomFrac)
    else:
        quarterPi = quarterPi + (topFrac/bottomFrac)
    count += 1
    bottomFrac += 2

print(quarterPi)
Pi = quarterPi * 4
print(Pi)