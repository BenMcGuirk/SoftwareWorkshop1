"""
In lucky sevens, a player rolls two dice with the aim of them adding to 7. If they do the player recieves $4, but if they don't
the player loses $1. 
Write a program that demonstrates the futility of playing the game. Your program should take as input the amount of money that
the player wants to put into the pot, and play the game until the pot is empty. At this point the program should print the number
rolls it took to break the player as well as the maximum amount of money in the pot at any time during the game.
"""
import random

moneyIn = int(input("How much money would you like to put in? "))
maxMoney = moneyIn
count = 0

while moneyIn > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:
        print("You won!")
        moneyIn += 4
        if moneyIn > maxMoney:
            maxMoney = moneyIn
    else:
        print("You lost")
        moneyIn -= 1
    print("$" + str(moneyIn))
    count += 1

print("It took ", str(count), "roll(s) to break the player")
print("The maximum amount of money at any one point was $", str(maxMoney))
