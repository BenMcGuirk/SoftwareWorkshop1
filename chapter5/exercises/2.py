"""
Write a program that allows the user to navigate lines of text in a file. The program should prompt the user for a filename 
and input the lines of text into a list. The program then enters a loop in which it prints the number of lines in the file and 
prompts the user for a line number. Actual line numbers range from 1 to the number of lines in the file. If the input is 0, 
the program quits. Otherwise, the program prints the line associated with that number.
"""
#copilot solution as I was feeling lazy
def main():
    filename = input("Enter a filename: ")
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close()

    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")

    print("The file has {} lines.".format(len(lines)))

    while True:
        line_num = int(input("Enter a line number or 0 to quit: "))
        if line_num == 0:
            break
        else:
            print(lines[line_num - 1])

main()