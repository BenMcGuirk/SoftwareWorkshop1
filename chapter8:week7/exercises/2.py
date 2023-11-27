"""
Create a Python program that handles multiple exceptions. The program should try to open a non-existent file and read an 
integer from it, thus potentially causing both FileNotFoundError and ValueError exceptions.
"""

try:
    f = open('file.txt', 'r')
except FileNotFoundError:
    print('File not found')
except ValueError:
    print('Value error')
else:
    print('No errors!')
finally:
    f.close()
    print('File has been closed')