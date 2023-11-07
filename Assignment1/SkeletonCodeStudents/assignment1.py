def clean_up():
    """
        f refers to text_to_clean.txt
        sf refers to student_names.txt
        use text to read in the appropriate file
        cleaned is used store the wanted characters
        :return: cleaned
        """
    f = open("text_to_clean.txt", "r")
    sf = open("student_names.txt", "w")
    text = f.read()
    cleaned = ""
    # lower case char, upper case char, blank, full stop - valid characters
    # insert code here to clean the file as per question 1
    # split the code line by line

    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or char == " " or char == "." or char == "\n":
            cleaned += char

    sf.write(cleaned)
    f.close()
    sf.close()
    return cleaned



def build_id():
    """
    f refers to the student_names.txt file created in clean_up()
    id_list is the list return with the id's created from the name / surname of each student
    :return: id_list
    """
    f = open("student_names.txt", "r")
    id_list = []
    # insert code here to create the id's as per question 2
    # split the code line by line
    # if name has three words - use initials as id 
    # if name has two words - use initials with X in between as id.
    for line in f:
        line = line.lower()
        line = line.split()
        if len(line) == 3:
            id_list.append(line[0][0] + line[1][0] + line[2][0])
        elif len(line) == 2:
            id_list.append(line[0][0] + "x" + line[1][0])
    f.close()
    print(id_list)
    return id_list


def validate_password(password):
    """
    illegal_password is the list that is built up showing the invalid parts of the password
    Validate the password to verify if it is legal or not as per Question 3
    There is a password.txt file given to you to verify invalid passwords
    :param password: make use of the password found in main(), the test file will also have additional passwords to test
    :return: illegal_password
    """

    """
    A valid password has the following:
    - at least 8 characters
    - at most 12 characters
    - at least one uppercase letter
    - at least one lowercase letter
    - contains only alphabetical characters, digits and the underscore character
    - it does not start with a digit
    - it does not contain any of the common passwords in password.txt 
    """

    f = open("password.txt", "r")
    text = f.read()

    illegal_password = []
    #insert code here to validate all the conditions of the password as per question 3
    if len(password) < 8:
        illegal_password.append("TOO SHORT")
    if len(password) > 12:
        illegal_password.append("TOO LONG")

    if not any('A' <= char <= 'Z' for char in password):
        illegal_password.append("NOT MIXED CASE")
    if not any('a' <= char <= 'z' for char in password):
        illegal_password.append("NOT MIXED CASE")

    if not all(('A' <= char <= 'Z' or 'a' <= char <= 'z' or char == '_' or '0' <= char <= '9') for char in password):
        illegal_password.append("WRONG CHARACTERS")

    if password[0].isdigit():
        illegal_password.append("LEADING DIGIT")

    if password in text:
        illegal_password.append("CANNOT MAKE USE OF THIS PASSWORD")

    f.close()
    return illegal_password


def create_unique(id_list):
    """
    Adhere to the instructions in question 4 to determine a unique id for each student
    Write the content of the unique ids to the file unique_ids.txt - open / close the file correctly
    Write the content of the emails created to the file create_emails.txt - - open / close the file correctly
    :param id_list: the id_list that was returned in build_id() is used here to create the unique ids
    :return: final_list is returned and this list contains all of the unique student ids
    """

    """
    Unique ID's are created as follows:
    - includes short id from Q2, with 0000 appended to the end (e.g. jxw0000).
    - if there is already a student with the same short id, then the number is incremented by 1 (e.g. jxw0001).
    """
    f = open("unique_ids.txt", "w")
    sf = open("create_emails.txt", "w")
    database = {}
    final_list = []
    email_list = []
    # insert code here to create unique ids
    for id in id_list:
        if id not in database:
            database[id] = 0000
            final_list.append(f"{id}{database[id]:04d}")
        else:
            database[id] += 1
            final_list.append(f"{id}{database[id]:04d}")

    for id in final_list:
        email_list.append(id + "@student.bham.ac.uk")

    for id in email_list:
        sf.write(id + "\n")
    
    for id in final_list:
        if id not in final_list[-1]:
            f.write(id + "\n")
        else:
            f.write(id) # this is to prevent a new line being added to the end of the file causing an error in function 7

    f.close()
    sf.close()
    return final_list


def create_short_address():
    """
    Open the addresses.txt file correctly where f = the file to be opened
    split the address up so that only the first part and the postcode make up the shorter address
    :return: split_addrs is returned where the address1, postcode make up the list - this list is used for validate_pcode()
    """
    f = open("addresses.txt", "r")
    text = f.read()
    split_addrs = []
    # insert code here to create the shorter address
    split_by_line = text.split("\n")
    split_by_comma = []
    for line in split_by_line:
        split_by_comma.append(line.split(","))

    for x in split_by_comma:
        split_addrs.append(x[0] + "," + x[-1])

    f.close()
    return split_addrs


def validate_pcode(split_addrs):
    """
    This function validates each character of the postcode
    :param split_addrs: this is passed from main(), obtained from the function create_short_address()
    :return: validate_pcode is a list that contains True False values for each postcode that is validated - see question 6
    """
    """
    Postcode validation:
    - must be 6 characters long
    - first character must be an uppercase letter
    - second third and fourth characters must be digits
    - fifth and sixth characters must be uppercase letters
    (assign each pcode with a unique number at the start)
    """
    validate_pcode = []
    # insert code here to validate each character of the postcode
    count = 0
    for addrs in split_addrs:
        isolatePcode = addrs.split(", ")
        validate_pcode.append(count)
        pcode = isolatePcode[1]
        if len(pcode) != 6:
            validate_pcode.append('False')
            pcode += '$$$$$$'
        else:
            validate_pcode.append('True')

        if not 'A' <= pcode[0] <= 'Z':
            validate_pcode.append('False')
        else:
            validate_pcode.append('True')

        if not '0' <= pcode[1] <= '9' or not '0' <= pcode[2] <= '9' or not '0' <= pcode[3] <= '9':
            validate_pcode.append('False')
        else:
            validate_pcode.append('True')

        if not 'A' <= pcode[4] <= 'Z' or not 'A' <= pcode[5] <= 'Z':
            validate_pcode.append('False')
        else:
            validate_pcode.append('True')

        count += 1

    return validate_pcode


def ids_addrs(short_addr):
    """
    This function reads in the unique_ids.txt file as f and creates a dictionary based on the id and the short address
    :param short_addr: passed in from main() - generated from create_short_address()
    :return: combo is the key / value pair, i.e. unique id and the short addr for each student

    call function 2, 4 and 5 before this function
    """
    f = open("unique_ids.txt", "r")
    ids = f.read()
    # reorder ids by 4-digit number size (mas0001 and mas0002 moved to the end)
    ids = ids.split("\n")
    ids_with_0 = []
    ids_without_0 = []   

    for id in ids:
        if id[-1] == "0":
            ids_with_0.append(id)
        else:
            ids_without_0.append(id) 

    ids = ids_with_0 + ids_without_0

    combo = {}
    # insert code here to create combo
    for x in range(len(ids)):
        combo[ids[x]] = [short_addr[x]]

    f.close()
    return combo
    


def main():
    id_list = []
    while True:
        print("\nStudent File Menu:")
        print("1. Perform clean up operation")
        print("2. Create ID's")
        print("3. Validate a Password")
        print("4. Create unique ID's")
        print("5. Reduce addresses")
        print("6. Validate postcode")
        print("7. Create ID with short address")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            clean_up()
        elif choice == '2':
            id_list = build_id()
        elif choice == '3':
            validate_password("1abcDE%")
        elif choice == '4':
            create_unique(id_list)
        elif choice == '5':
            short_addr = create_short_address()
        elif choice == '6':
            validate_pcode(short_addr)
        elif choice == '7':
            ids_addrs(short_addr)
        elif choice == '8':
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()



