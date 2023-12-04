"""
    - the variables rows and columns indicate the number of rows and the number of columns
      that becomes the board, as per the instructions
    - the values (5 x 5) below can be changed as you test your code
    - a valid board will always have an odd number of rows and columns e.g.5 or 7
    - rows and columns must always have the same number
"""
rows = 5
columns = 5

#you may include other global variables if you need to

def generate_board():
    board = []
    board = [' '] * (rows * columns)
    """
        insert code here to create a board as per the instructions
    
    """
    return (board)
#generate_board()


def print_board(board):

    for j in range(len(board)):
        if j == len(board) - 1: #print board with extra code for formatting reasons
            print(board[j])
        elif (j + 1) % (columns) == 0 and j != 0:
            print(board[j])
        elif j == 0:
            print(board[j], '|', end=' ')
        else:
            print(board[j], '|', end=' ')
    
        
    """
        insert code here to print the board as per the instructions

    """
#print_board(generate_board())

def place_row_col(board, option, a_row, a_col):
    message = " "
    position = None
    turn = 'X' #game must start with X
    if option != 'X' or 'O':
        message += "Option isn't an X or an O"
    elif position != None:
        mesage += "Illegal move, this position already holds an X or an O"
    elif option != turn:
        message += "It's not your turn"
    else:
        #formula for board index/position based on row and column
        #(a_row - 1) * (num columns) + a_col
        #eg cell 8 (5x5 grid, row 2, col 3): (1) x (5) + 3
        cellSelected = (a_row - 1) * (columns) + a_col
        position = cellSelected
        board[position] = turn
        message += "Move successfully played"
    
    

    #each time function is called, turn changes.
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    """
        insert code here to place either an 'X' or an 'O' on the board as per the instructions
        You can assume that there will only be 1 message sent
        message = "Move successfully played"
        message = "Option isn't an X or an O"
        message = "It's not your turn"
        message = "Illegal move, this position already holds an X or an O"

    """
    return (board, message)

def check_win(board):
    is_winner = " "
    """
            - insert code here to determine a winner based on the rules as per the instructions 
              in the question
            - examples of messages could be:
              - X wins on the corners
              - O wins on the diagonal
              - X wins on the reversed diagonal
              - O wins on the cross
    """
    #corners win indexes 1, columns, 
    #corners start
    if board[1] == 'X' and board[columns] == 'X' and board[(rows -1) * columns + 1] == 'X' and board[-1] == 'X':
        is_winner += 'X wins on the corners'
    elif board[1] == 'O' and board[columns] == 'O' and board[(rows -1) * columns + 1] == 'O' and board[-1] == 'O':
        is_winner += 'O wins on the corners'
    #corners end

    #diagonal start
    index = 1
    diagonalIncrement = rows+1 
    diagonalWinnerX = False
    diagonalWinnerO = False
    for j in range(rows):
        if board[index] == 'X':
            diagonalWinnerX = True
        else: 
            diagonalWinnerX = False
            break
        index += diagonalIncrement
    if diagonalWinnerX == True:
        is_winner += 'X wins on the diagonal'

    index = 1
    for j in range(rows):
        if board[index] == 'O':
            diagonalWinnerO = True
        else:
            diagonalWinnerO = False
            break
        index += diagonalIncrement
    if diagonalWinnerO == True:
        is_winner += 'O wins on the diagonal'
    #diagonal end

    #reverse diagonal start
    index = 1
    diagonalIncrement = rows-1 #main difference of reverse is index increments by numRows -1 now not numRows +1
    rDiagonalWinnerX = False
    rDiagonalWinnerO = False
    for j in range(rows):
        if board[index] == 'X':
            rDiagonalWinnerX = True
        else: 
            rDiagonalWinnerX = False
            break
        index += diagonalIncrement
    if rDiagonalWinnerX == True:
        is_winner += 'X wins on the reverse diagonal'

    index = 1
    for j in range(rows):
        if board[index] == 'O':
            rDiagonalWinnerO = True
        else:
            rDiagonalWinnerO = False
            break
        index += diagonalIncrement
    if rDiagonalWinnerO == True:
        is_winner += 'O wins on the reverse diagonal'
    #rd end

    #cross start
    index1 = int(rows / 2) #start at middle column first row
    index2 = int(columns / 2) #start middle row first column
    crossIncrement1 = rows #vertical cross increment is number of rows as its same column just one row down each iteration
    crossIncrement2 = 1 #horizontal cross increment
    crossWinnerX = False
    crossWinnerO = False
    for j in range(rows):
        if board[index1] == 'X':
            crossWinnerX = True
        else: 
            crossWinnerX = False
            break
        index1 += crossIncrement1
    if crossWinnerX == True:
        is_winner += 'X wins on the cross'

    for j in range(rows):
        if board[index2] == 'X':
            crossWinnerX = True
        else: 
            crossWinnerX = False
            break
        index2 += crossIncrement2
    if crossWinnerX == True:
        is_winner += 'X wins on the cross'

    index1 = int(rows / 2)
    for j in range(rows):
        if board[index1] == 'O':
            crossWinnerO = True
        else:
            crossWinnerO = False
            break
        index1 += crossIncrement1
    if crossWinnerO == True:
        is_winner += 'O wins on the cross'

    index2 = int(columns / 2)
    for j in range(rows):
        if board[index2] == 'O':
            crossWinnerO = True
        else:
            crossWinnerO = False
            break
        index2 += crossIncrement2
    if crossWinnerO == True:
        is_winner += 'O wins on the cross'
    #cross end

    return is_winner

"""
    - make use of the simulated board-game below to play the game
    - each time you test it is mandatory to first execute generate_board() 
      and secondly print_board(game_board) - this is provided to you for each test case
    - each test case is separate, clear the comments below for one test case, test it and 
      move on systematically
"""

"""
   #play one move
   #message = "Move successfully played"
   
game_board = generate_board()
game_board, message = place_row_col(game_board, "X", 2, 3)
print_board(game_board)
print(message)

"""

"""
    #check for an 'X' that follows a 'O'
    #message = "Move successfully played"

game_board = generate_board()
game_board, message = place_row_col(game_board, "X", 1, 1)
game_board, message = place_row_col(game_board, "O", 2, 2)
print_board(game_board)
print(message)

"""

"""
   #play a move that is not an X or an O
   #message = "Option isn't X or O"
   
game_board = generate_board()
game_board, message = place_row_col(game_board, "H", 2, 3)
print_board(game_board)
print(message)

"""

"""
    #check for an 'X' that follows a 'X'
    #message = "It's not your turn"
    
game_board = generate_board()
game_board, message = place_row_col(game_board, "X", 1, 1)
game_board, message = place_row_col(game_board, "X", 2, 2)
print_board(game_board)
print(message)

"""

"""
    #check for an illegal move
    #message = "Illegal move, this position already holds an X or an O"
    
game_board = generate_board()
game_board, message = place_row_col(game_board, "X", 0, 0)
game_board, message = place_row_col(game_board, "O", 2, 2)
game_board, message = place_row_col(game_board, "X", 0, 0)
print_board(game_board)
print(message)

"""

"""
 ----------------Test for Wins given the test cases below-----------------
 As per the rules these are the options:
 is_winner = "O wins on the corners"
 is_winner = "O wins on the diagonal"
 is_winner = "X wins on the reversed diagonal"
 is_winner = "O wins on the cross"
"""

"""
    #a board that has no winner
    #is_winner = " "
game_board = generate_board()
game_board, message = place_row_col(game_board, "X", 3, 4)
game_board, message = place_row_col(game_board, "O", 4, 2)
is_winner = check_win(game_board)
print_board(game_board)
print(is_winner)
"""

"""
    #check for a corner win
    #is_winner = "O wins on the corners"
    
game_board = generate_board()
game_board, message = place_row_col(game_board, "X", 0, 1)
game_board, message = place_row_col(game_board, "O", 0, 0)
game_board, message = place_row_col(game_board, "X", 0, 2)
game_board, message = place_row_col(game_board, "O", 0, 4)
game_board, message = place_row_col(game_board, "X", 1, 4)
game_board, message = place_row_col(game_board, "O", 4, 0)
game_board, message = place_row_col(game_board, "X", 2, 1)
game_board, message = place_row_col(game_board, "O", 4, 4)
is_winner = check_win(game_board)
print_board(game_board)
print(is_winner)

"""

"""
    #check for a diagonal win
    #is_winner = "O wins on the diagonal"
    
game_board = generate_board()
game_board, message = place_row_col(game_board, "X", 0, 1)
game_board, message = place_row_col(game_board, "O", 0, 0)
game_board, message = place_row_col(game_board, "X", 0, 2)
game_board, message = place_row_col(game_board, "O", 1, 1)
game_board, message = place_row_col(game_board, "X", 1, 4)
game_board, message = place_row_col(game_board, "O", 2, 2)
game_board, message = place_row_col(game_board, "X", 2, 1)
game_board, message = place_row_col(game_board, "O", 3, 3)
game_board, message = place_row_col(game_board, "X", 4, 1)
game_board, message = place_row_col(game_board, "O", 4, 4)
is_winner = check_win(game_board)
print_board(game_board)
print(is_winner)

"""

"""
    #check for a reversed diagonal win
    #is_winner = "X wins on the reversed diagonal"
    
game_board = generate_board()
game_board, message = place_row_col(game_board, "X", 0, 4)
game_board, message = place_row_col(game_board, "O", 0, 1)
game_board, message = place_row_col(game_board, "X", 1, 3)
game_board, message = place_row_col(game_board, "O", 0, 2)
game_board, message = place_row_col(game_board, "X", 2, 2)
game_board, message = place_row_col(game_board, "O", 1, 4)
game_board, message = place_row_col(game_board, "X", 3, 1)
game_board, message = place_row_col(game_board, "O", 2, 1)
game_board, message = place_row_col(game_board, "X", 4, 0)
game_board, message = place_row_col(game_board, "O", 4, 1)
is_winner = check_win(game_board)
print_board(game_board)
print(is_winner)

"""

"""
    #check for a cross win
    #is_winner = "O wins on the cross"
    
game_board = generate_board()
game_board, message = place_row_col(game_board, "X", 0, 3)
game_board, message = place_row_col(game_board, "O", 2, 2)
game_board, message = place_row_col(game_board, "X", 1, 3)
game_board, message = place_row_col(game_board, "O", 2, 1)
game_board, message = place_row_col(game_board, "X", 1, 0)
game_board, message = place_row_col(game_board, "O", 2, 3)
game_board, message = place_row_col(game_board, "X", 3, 1)
game_board, message = place_row_col(game_board, "O", 1, 2)
game_board, message = place_row_col(game_board, "X", 0, 0)
game_board, message = place_row_col(game_board, "O", 3, 2)
is_winner = check_win(game_board)
print_board(game_board)
print(is_winner)

"""

"""
 ----------------Test for Board 3X3------------------------------------------------
 Remember to change the values of rows and columns variables
 Comment out all test cases above before changing board sizes, otherwise this will result in errors
"""

"""
    #check for a reversed diagonal win 3X3 board
    #is_winner = "O wins on reversed diagonal"

game_board = generate_board()
game_board, message = place_row_col(game_board, "X", 0, 0)
game_board, message = place_row_col(game_board, "O", 0, 2)
game_board, message = place_row_col(game_board, "X", 0, 1)
game_board, message = place_row_col(game_board, "O", 1, 1)
game_board, message = place_row_col(game_board, "X", 1, 2)
game_board, message = place_row_col(game_board, "O", 2, 0)
is_winner = check_win(game_board)
print_board(game_board)
print(is_winner)

"""

"""
 ----------------Test for Board 7X7------------------------------------------------
 Remember to change the values of rows and columns variables
 Comment out all test cases above before changing board sizes, otherwise this will result in errors
"""

"""
    #check for a corner win 7X7 board
    #is_winner = "O wins on the corners"

game_board = generate_board()
game_board, message = place_row_col(game_board, "X", 0, 1)
game_board, message = place_row_col(game_board, "O", 0, 0)
game_board, message = place_row_col(game_board, "X", 0, 2)
game_board, message = place_row_col(game_board, "O", 0, 6)
game_board, message = place_row_col(game_board, "X", 1, 4)
game_board, message = place_row_col(game_board, "O", 6, 0)
game_board, message = place_row_col(game_board, "X", 2, 1)
game_board, message = place_row_col(game_board, "O", 6, 6)
is_winner = check_win(game_board)
print_board(game_board)
print(is_winner)

"""