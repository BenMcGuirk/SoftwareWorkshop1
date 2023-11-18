"""
Write a script that inputs a line of encypted text and a distance value and outputs plaintext using a Caesar cipher. 
The script should work for any printable characters.
"""
code = input("Enter your code: ")
distance = int(input("Enter the distance: "))
plainText = ""

for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - distance - (ord('a') - ordValue - 1)
    plainText += chr(cipherValue)

print(plainText)

# new solution
code = input("Enter your code: ")
distance = int(input("Enter the distance: "))
plainText = ""

for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < ord('a'):
        overlap = ord('a') - cipherValue
        cipherValue = ord('z') - overlap + 1
    plainText += chr(cipherValue)

print(plainText)

# both solutions working