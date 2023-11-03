"""
Teachers are paid on a schedule that provides a salary based on their number of years of experience. A beginning teacher may be 
paid $30,000 for the first year. For each year of experience the teacher recieves a 2% increase of the preceding value
(up to 10 years).
Write a program that displays the salary schedule in tabular format. The inputs are starting salary, percentage increase and 
number of years experience. Each row should contain the year number and the salary for that year.
"""
startingSalary = float(input("Enter the starting salary: "))
percentageIncrease = float(input("Enter the percentage increase: "))
compound = 1 + (percentageIncrease/100)

print("Year", "Salary")
print("1", "  ", "$" + str("{:.2f}".format(startingSalary, 2)))
print("2", "  ", "$" + str("{:.2f}".format(startingSalary * compound)))
print("3", "  ", "$" + str("{:.2f}".format(startingSalary * compound**2)))
print("4", "  ", "$" + str("{:.2f}".format(startingSalary * compound**3)))
print("5", "  ", "$" + str("{:.2f}".format(startingSalary * compound**4)))
print("6", "  ", "$" + str("{:.2f}".format(startingSalary * compound**5)))
print("7", "  ", "$" + str("{:.2f}".format(startingSalary * compound**6)))
print("8", "  ", "$" + str("{:.2f}".format(startingSalary * compound**7)))
print("9", "  ", "$" + str("{:.2f}".format(startingSalary * compound**8)))
print("10", " ", "$" + str("{:.2f}".format(startingSalary * compound**9)))