#write a script that prompts the user for two text files. The content of the first file should be added to the second file.
#the script should work with any two text files.
#the names of the two files should be provided by the user.

#open the first file
file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the second file: ")

#open the second file
with open(file1, 'r') as f1:
    file1_data = f1.read()

with open(file2, 'a') as f2:
    f2.write(file1_data)