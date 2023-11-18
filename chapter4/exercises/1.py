"""
Write a script that inputs a line of plain text and a distance value and outputs an encrypted text using a Caesar cipher. 
The script should work for any printable characters.
"""

plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - (ord('z') - ordValue + 1)
    code += chr(cipherValue)
print(code)

# attempt at another solution

plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + (cipherValue - ord('z') - 1)
    code += chr(cipherValue)
print(code)

# a second way of writing the second method:
plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
        overlap = cipherValue - ord('z')
        cipherValue = ord('a') + (overlap - 1)
    code += chr(cipherValue)
print(code)

# all solutions working