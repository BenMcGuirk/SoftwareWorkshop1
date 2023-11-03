"""
The credit plan at TidBit computer store specifies a 10% down payment and an anual interest rate of 12%. Monthly payments are 5%
of the listed purchase price, minus the downpayment. Write a program that takes the purchase price as input. The program should
display a table with headers of a payment schedule. Each row should contain:
- month number
- current total balance owed
- amount of principal owed for that amount
- payment for that month
- balance remaining after payment

Interest equals balance * rate / 12. The amount of principal for a month is equal to the monthly payment minus the interest owed.

Example 1:

Purchase price = $10,000
Down payment = $1000
Interest rate 12%
Monthly payments = $450

Month1:
Month number = 1
Current total balance owed = $9,000
Principal = $360
Payment = $450
Balance remaining = $8640

Balance = previous month balance - principal
"""

purchasePrice = int(input("Enter the purchase price: "))
downPayment = purchasePrice/10
remainingBalance = purchasePrice - downPayment
monthlyPayment = (purchasePrice - downPayment) * 0.05
month = 0 

print("Month | Total owed | Principal owed | Payment | Balance remaining")

while remainingBalance > 0:
    month += 1
    totalOwed = remainingBalance
    interest = (remainingBalance * 0.12) / 12
    principal = monthlyPayment - interest
    
    if totalOwed < principal:
        principal = totalOwed
        monthlyPayment = totalOwed
    remainingBalance -= principal
    print(str("{:.2f}".format(month)), "     ", str("{:.2f}".format(totalOwed, 2)), "     ", "$" + str("{:.2f}".format(principal, 2)), "        ", "$" + str("{:.2f}".format(monthlyPayment, 2)), "          ", "$" + str("{:.2f}".format(remainingBalance, 2)))