"""
Use the strategy of decimal to binary conversion and the bit shift left operation to code a new encryption algorithm. The
algorithm should add 1 to each character's numeric ASCII value, convert it to a bit string, and shift the bits one place to the
left. 
"""
text = input("Enter your text: ")
code = ''
for ch in text:
    #convert each character to numeric ASCII value and add 1.
    ordValue = ord(ch)
    cipherValue = ordValue + 1
    if cipherValue > ord('z'):
        cipherValue = ord('a') + 1 - (ord('z') - ordValue + 1)

    #convert to bit string
    decimal = cipherValue
    binary = ''
    if decimal == 0:
        print(0)
    else:
        while decimal > 0:
            remainder = decimal % 2
            decimal = decimal / 2
            decimal = int(decimal)
            binary = str(int(remainder)) + binary

    #shift bits left one place
    leftShift = list(binary)
    leftShift.append(leftShift.pop(0))
    result = ''.join(leftShift)
    
    code += result
    #add space after each chr
    code += ' '
#print(code)
print(code)