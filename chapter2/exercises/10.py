"""
An employees total pay is their hourly wage multiplied by the number of regular hours worked plus overtime pay.
Overtime pay is 1.5 times regular hourly pay.
Write a program that takes the hourly wage, regular hours and overtime hours and return the total weekly pay.
"""
hourlyWage = float(input("Enter hourly wage: "))
numHours = float(input("Enter number of regular hours: "))
numOvertimeHours = float(input("Enter number of overtime hours: "))

totalWeekPay = (hourlyWage * numHours) + ((hourlyWage * 1.5) * numOvertimeHours)
print("Total pay = " + str(totalWeekPay))