"""
Write a program that lets a user input a series of numbers until they press enter. After the user presses enter the program
should print the sum of the numbers and their average.
"""
numbers = int(input("Enter your numbers, press ENTER when finished: "))

numList = list(str(numbers)) #initalise number list   
#print(numList) (test)

sum = 0
for num in numList:
    sum += int(num)

average = sum / len(numList)
print("Sum =", sum, "Average =", average)