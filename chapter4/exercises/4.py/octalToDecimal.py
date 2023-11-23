"""
Convert octal to decimal
"""
octal = str(input("Enter your octal number: "))
decimal = 0
exponent = len(octal) - 1
for x in octal:
    decimal = decimal + int(x) * 8 ** exponent
    exponent = exponent - 1
print(decimal)