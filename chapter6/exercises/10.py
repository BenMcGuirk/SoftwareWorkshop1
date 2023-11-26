"""
Define and test a function myRange. This function should behave like Pythons standard range function, with the required and 
optional arguments. Do not use the range function in your implementation! (Hints: Study Pythons help on range to determine 
the names, positions, and what to do with your functions parameters. Use a default value of None for the two optional parameters. 
If these parameters both equal None, then the function has been called with just the stop value. If just the third parameter 
equals None, then the function has been called with a start value as well. Thus, the first part of the functions code 
establishes what the values of the parameters are or should be. The rest of the code uses those values to build a list by 
counting up or down.)
"""

#syntax: range(start, stop, step)

def myRange(stop, start=0, step=1):
    while stop > start:
        print(start)
        start += step

myRange(5, 0)
myRange(7, 0, 2)
myRange(3, 2)
