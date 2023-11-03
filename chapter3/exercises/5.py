"""
Write a program that predicts population growth for a biologist. The inputs will be the initial number of organisms, the rate of
growth, the number of hours it takes to achieve this rate and a number of hours during which the population grows. 

For example a population may start at 500. A growth rate of 2 and a growth period of 6 hours. This means that after 6 hours the
population will be 1000, and after 12 hours it will be 2000. **EXPONENTIAL GROWTH**
"""

initialNum = float(input("Enter the initial number of organisms: "))
growthRate = float(input("Enter the growth rate: "))
growthRateHours = float(input("Enter the number of hours to achieve the growth rate: "))
growthHours = float(input("Enter the number of hours the population grows for: "))

exponent = growthHours / growthRateHours

#formula - endPopulation = initialNum * growthRate^exponent
endPopulation = initialNum * growthRate ** exponent
print("End population = " + str(endPopulation))