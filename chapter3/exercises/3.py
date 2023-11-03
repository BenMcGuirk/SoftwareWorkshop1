"""
Modify the guessing game of sectoin 3.5 so that the user thinks of a number that the computer has to guess. 
The computer must make the minmum possible of guesses (implement binary search).
"""
import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
userNumber = int(input("Enter your number: "))
count = 0

#print(list(range(smaller, larger + 1))) testing array formation
numArray = list(range(smaller, larger + 1))
left = 0
right = len(numArray) - 1


while True:
    count += 1
    mid = math.floor((left + right) / 2)
    computerNumber = numArray[mid]
    print("Computer's guess is: " + str(computerNumber) + ".")
    if computerNumber < userNumber:
        print("TOO LOW!")
        left = mid + 1
    elif computerNumber > userNumber:
        print("TOO HIGH")
        right = mid
    else:
        print("CORRECT! The computer got it in " + str(count) + " tries.")
        break