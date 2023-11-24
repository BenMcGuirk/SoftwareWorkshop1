"""
A file concordance tracks the unique words in a file and their frequencies. Write a program that displays a concordance for a 
file. The program should output the unique words and their frequencies in alphabetical order.
"""
inputFile = input("Enter file name: ")
file = open(inputFile, 'r')
content = file.read()
text = content.split(' ')
text.sort()
data = {}
for word in text:
    if word in data:
        data[word] += 1
    else:
        data[word] = 1
for key, value in data.items():
    print(key, value)