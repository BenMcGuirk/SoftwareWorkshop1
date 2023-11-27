"""
Write a python program that uses a try-except-finally block to open and read a file. The program should handle any 
FileNotFoundError exceptions that occur if the file does not exist, and use the finally block to confirm that the file 
has been closed.
"""
try:
    f = open('1py.txt', 'r')
except FileNotFoundError:
    print('File does not exist')
else: 
    print('No errors!')
finally:
    f.close()
    print('File has been closed')