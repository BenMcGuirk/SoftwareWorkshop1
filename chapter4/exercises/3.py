"""
Modify the scripts from 1 and 2 to encrypt and decrypt entire files of text.
"""
import time
distance = int(input("Enter the distance value: "))
print('Encrypting file...')
time.sleep(1)
# open and read file
f = open('project3.txt', 'r')
text = f.read()
text = text.lower()
text = text.split()
code = ''
for word in text:
    for ch in word:
        ch.lower()
        ordValue = ord(ch)
        cipherValue = ordValue + distance
        if cipherValue > ord('z'):
            overlap = cipherValue - ord('z')
            cipherValue = ord('a') + (overlap - 1)
        code += chr(cipherValue)
    code += ' '
print(code)

print('Decrypting file...')
time.sleep(1)
plainText = ''
for ch in code:
    if not ch.isalpha():
        plainText += ' '
        continue
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < ord('a'):
        overlap = ord('a') - cipherValue
        cipherValue = ord('z') - overlap + 1
    plainText += chr(cipherValue)

print(plainText)