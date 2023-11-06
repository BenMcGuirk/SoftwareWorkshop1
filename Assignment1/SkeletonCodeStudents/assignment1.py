def clean_up():
    """
        f refers to text_to_clean.txt
        sf refers to student_names.txt
        use text to read in the appropriate file
        cleaned is used store the wanted characters
        :return: cleaned
        """
    f = ""
    sf = ""
    text = f.read()
    cleaned = ""
    # lower case char, upper case char, blank, full stop - valid characters
    # insert code here to clean the file as per question 1
    return cleaned

def build_id():
    """
    f refers to the student_names.txt file created in clean_up()
    id_list is the list return with the id's created from the name / surname of each student
    :return: id_list
    """
    f = ""
    id_list = []
    #insert code here to create the id's as per question 2
    return id_list


def validate_password(password):
    """
    illegal_password is the list that is built up showing the invalid parts of the password
    Validate the password to verify if it is legal or not as per Question 3
    There is a password.txt file given to you to verify invalid passwords
    :param password: make use of the password found in main(), the test file will also have additional passwords to test
    :return: illegal_password
    """
    illegal_password = []
    #insert code here to validate all the conditions of the password as per question 3
    return illegal_password
def create_unique(id_list):
    """
    Adhere to the instructions in question 4 to determine a unique id for each student
    Write the content of the unique ids to the file unique_ids.txt - open / close the file correctly
    Write the content of the emails created to the file create_emails.txt - - open / close the file correctly
    :param id_list: the id_list that was returned in build_id() is used here to create the unique ids
    :return: final_list is returned and this list contains all of the unique student ids
    """
    final_list = []
    # insert code here to create unique ids
    return final_list
def create_short_address():
    """
    Open the addresses.txt file correctly where f = the file to be opened
    split the address up so that only the first part and the postcode make up the shorter address
    :return: split_addrs is returned where the address1, postcode make up the list - this list is used for validate_pcode()
    """
    f = " "
    text = f.read()
    split_addrs = []
    # insert code here to create the shorter address
    return split_addrs

def validate_pcode(split_addrs):
    """
    This function validates each character of the postcode
    :param split_addrs: this is passed from main(), obtained from the function create_short_address()
    :return: validate_pcode is a list that contains True False values for each postcode that is validated - see question 6
    """
    validate_pcode = []
    # insert code here to validate each character of the postcode
    return validate_pcode

def ids_addrs(short_addr):
    """
    This function reads in the unique_ids.txt file as f and creates a dictionary based on the id and the short address
    :param short_addr: passed in from main() - generated from create_short_address()
    :return: combo is the key / value pair, i.e. unique id and the short addr for each student
    """
    f = ""
    ids = f.read()
    combo = {}
    # insert code here to create combo
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



