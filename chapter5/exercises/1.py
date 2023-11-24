"""
Create set of functions to compute the median and mode of a set of numbers. Also include a function names mean, which computes
the mean. Each function should expect a list of numbers and return a single number. Each function should return 0 if the list is
empty. Include a main function that tests the three functions with a given list.
"""
nums = input("Enter number list: ")
numList = [int(char) for char in nums]

def mode(numbers):
    data = {}
    for num in numbers:
        if num in data:
            data[num] += 1
        else:
            data[num] = 1
    max = 0
    modeVal = None
    for key, value in data.items():
        if value > max:
            max = value
            modeVal = key
    print('Mode =', modeVal) 

def median(numbers):
    medNum = None
    numbers.sort()
    if len(numbers) % 2 == 1:
        medNum = numbers[int(len(numbers)/2)]
    else:
        medNum = (numbers[int(len(numbers)/2) - 1] + numbers[int(len(numbers)/2)]) / 2
    print('Median =', medNum) 
   
def mean(numbers):
    sum = 0
    for num in numbers:
        sum += num
    m = sum/len(numbers)
    print('Mean =', m) 


def main(list):
    mode(list)
    median(list)
    mean(list)

main(numList)

# copilot solution 

# def mean(numbers):
#     if len(numbers) == 0:
#         return 0
#     else:
#         total = 0
#         for num in numbers:
#             total += num
#         return total / len(numbers)
#
# def median(numbers):
#     if len(numbers) == 0:
#         return 0
#     else:
#         numbers.sort()
#         if len(numbers) % 2 == 1:
#             return numbers[len(numbers) // 2]
#         else:
#             middle1 = numbers[len(numbers) // 2]
#             middle2 = numbers[len(numbers) // 2 - 1]
#             return (middle1 + middle2) / 2
#
# def mode(numbers):
#     if len(numbers) == 0:
#         return 0
#     else:
#         data = {}
#         for num in numbers:
#             if num in data:
#                 data[num] += 1
#             else:
#                 data[num] = 1
#         max = 0
#         modeVal = None
#         for key, value in data.items():
#             if value > max:
#                 max = value
#                 modeVal = key
#         return modeVal
#
# def main():
#     nums = input("Enter numbers: ")
#     numList = [int(num) for num in nums.split()]
#     print("Mean:", mean(numList))
#     print("Median:", median(numList))
#     print("Mode:", mode(numList))
#
# main()