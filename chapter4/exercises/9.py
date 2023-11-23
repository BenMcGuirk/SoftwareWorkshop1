"""
Write a script that compares the contents of two files, returns 'Yes' if they are identicle, and 'No' if not as well as the 
first line where they differ.
"""

file1 = '9py1.txt'
file2 = '9py2.txt'

with open(file1, 'r') as f1:
    text1 = f1.read()

with open(file2, 'r') as f2:
    text2 = f2.read()

text1 = text1.split('\n')
text2 = text2.split('\n')

for line1, line2 in zip(text1, text2):
    for char1, char2 in zip(line1, line2):
        if char1 != char2:
            print('No')
            print(line1 + '\n' + line2)
            break
    else:
        print('Yes')