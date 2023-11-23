"""
Write two bit shift scripts, shiftLeft and shiftRight. Make sure the wrapping takes place when bits are at the end of the bit
string.
"""
bitString = input("Enter bitstring: ")
rightShift = ''
def shiftLeft(bitString):
    leftShift = list(bitString)
    leftShift.append(leftShift.pop(0))
    result = ''.join(leftShift)
    print('Left shift: ', result)

def shiftRight(bitString):
    rightShift = list(bitString)
    rightShift.insert(0, rightShift.pop())
    result = ''.join(rightShift)
    print('Right shift: ', result)

shiftLeft(bitString)
shiftRight(bitString)