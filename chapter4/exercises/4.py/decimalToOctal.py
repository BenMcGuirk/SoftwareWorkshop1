"""
Convert decimal to octal
"""
decimal = int(input("Enter your decimal number: "))
octal = ''
if decimal == 0:
    print(0)
else:
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal / 8
        decimal = round(decimal, 0)
        octal = octal + str(int(remainder))
print(octal)