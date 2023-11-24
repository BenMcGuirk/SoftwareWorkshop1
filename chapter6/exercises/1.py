"""
Package Package Newton's method for approximating square roots (Case Study 3.6) in a function named newton. 
This function expects the input number as an argument and returns the estimate of its square root. 
The script should also include a main function that allows the user to compute square roots of inputs until she 
presses the enter/return key.
"""
def newton(num, initialEstimate = 1.0):
    estimate = initialEstimate
    estimate = (estimate + num / estimate) / 2
    print(estimate)
    return estimate


def main():
    num = float(input("Enter your number: "))
    estimate = 1.0
    while True:
        option = input("Press y to continue, enter to quit: ")
        if not option:
            break
        elif option.lower() == 'y':
            estimate = newton(num, estimate)
        else:
            print("Invalid key")


main()

"""
Elena complains that the recursive newton function in Project 2 includes an extra argument for the estimate. The functions 
users should not have to provide this value, which is always the same, when they call this function. Modify the definition of the 
function so that it uses a keyword parameter with the appropriate default value for this argument, and call the function without 
a second argument to demonstrate that it solves this problem.
"""
