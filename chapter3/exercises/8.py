largeNumber = int(input('Enter larger number: '))
smallNumber = int(input('Enter smaller number: '))

#print(largeNumber % smallNumber)

while(smallNumber != 0):
    remainder = largeNumber % smallNumber
    largeNumber = smallNumber
    smallNumber = remainder

print('GCD is', largeNumber)