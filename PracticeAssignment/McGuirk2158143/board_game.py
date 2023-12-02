import random
def generate_square_board():
    """
    change square_board below to reflect the 2 X 2 board
    insert code here to generate a square board of 2 X 2 with zeros
    a. The board is always a square board with dimensions of 2 x 2. 
    b. Make use of the variable square_board given in the function and complete the 
    necessary code required to generate a board as a list (you wont see the board 
    yet). Each row / column should contain a zero: see question 2 for an example. 
    c. Return the square_board.
    """
    square_board = [['0', '0'], ['0', '0']]
    return square_board

def print_board(square_board):
    for row in square_board:
        print('|',row[0], '|', row[1], '|')
    """
    :param square_board:
    print the board as instructed
    """

def generate_numbers(square_board):
    """
    :param square_board:
    generate the random numbers to replace all zeros on the board
    """
    for i in range(2):
        for j in range(2):
            square_board[i][j] = random.randint(1, 9)
    return square_board

def calculate_win(square_board):
    message = " "
    """
    :param square_board: 
    determine a win
    a. A win is if the sum of all 4 numbers totals 10, 20, 30, 40, 50, etc. 
    b. Return the message -> “There is a win” or “No win”. 
    c. For example there is a win if 
    the sum of the numbers add up to 40.
    message = "There is a win"
    message = "No win"
   """
    sum = 0
    for i in range(2):
        for j in range(2):
            sum += square_board[i][j]
    if sum % 10 == 0:
        message = "There is a win"
    else:
        message = "No win"
    return (message)

square_board = generate_square_board()
generate_numbers(square_board)
print_board(square_board)
message = calculate_win(square_board)
print(message)