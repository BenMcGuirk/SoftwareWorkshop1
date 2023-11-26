"""
Write a program that computes and prints the average of the numebrs in a text file. You should make use of two higher order 
functions to simplify the design.
"""
file = open('9py.txt', 'r')
text = file.read()

def average(tfile):
    sum = 0
    for num in text:
        sum += int(num)
    avg = sum / len(text)
    print(avg)
    
average(text)

#copilot solution

def average2(tfile):
    nums = list(map(int, tfile.split()))
    return sum(nums) / len(nums)
