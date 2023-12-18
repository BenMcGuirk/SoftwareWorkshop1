"""
    - the variables rows and columns indicate the number of rows and the number of columns
      that becomes the board, as per the instructions
    - the values (5 x 5) below can be changed as you test your code

"""
rows = 5
columns = 5

#you may include other global variables if you need to

def generate_board():
    board = []
    """
        insert code here to create a board as per the instructions
    
    """
    board = [[' ' for i in range(columns)] for j in range(rows)]
    return (board)

def print_board(board):
    """
        insert code here to print the board as per the instructions
        include separators between the rows and columns as per the instructions
    """
    """
    for i in range(rows):
        for j in range(columns):
            print(board[i][j], end=' ')
        print()
    """
    for i in range(rows):
        for j in range(columns - 1):
            print(board[i][j], '|', end=' ')
        print(board[i][columns - 1])

count = 0
turn = ""
def place_row_col(board, option, a_row, a_col):
    message = " "
    """
        insert code here to place either an 'X' or an 'O' on the board as per the instructions
        You can assume that there will only be 1 message sent
        message = "Move successfully played"
        message = "Option isn't an X or an O"
        message = "It's not your turn"
        message = "Illegal move, this position already holds an X or an O"

    """
    global turn
    global count
    if option == "X" or option == "O":
        if count == 0:
            turn = "X"
        if option != turn:
            message = "It's not your turn"
        elif board[a_row][a_col] == ' ':
            board[a_row][a_col] = option
            message = "Move successfully played"
        elif board[a_row][a_col] == 'X' or board[a_row][a_col] == 'O':
            message = "Illegal move, this position already holds an X or an O"
        if message == "Move successfully played":
            if option == "X":
                turn = "O"
            else:
                turn = "X"
    else:
        message = "Option isn't an X or an O"
    count += 1



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
    #must be able to check win for any size board
    #-----------------check for a corner win-----------------
    if board[0][0] == 'X' and board[0][columns - 1] == 'X' and board[rows - 1][0] == 'X' and board[rows - 1][columns - 1] == 'X':
        is_winner = "X wins on the corners"
        return is_winner
    if board[0][0] == 'O' and board[0][columns - 1] == 'O' and board[rows - 1][0] == 'O' and board[rows - 1][columns - 1] == 'O':
        is_winner = "O wins on the corners"
        return is_winner
    
    #-----------------check for a diagonal win-----------------
    xDiagonal = False
    oDiagonal = False  
    #loop for x
    for x in range(rows):
        if board[x][x] != 'X':
            is_winner = " "
            xDiagonal = False
            break
        else:
            xDiagonal = True
    if xDiagonal == True:
        is_winner = "X wins on the diagonal"
        return is_winner
        
    #loop for o
    for x in range(rows):
        if board[x][x] != 'O':
            is_winner = " "
            oDiagonal = False
            break
        else:
            oDiagonal = True
    if oDiagonal == True:
        is_winner = "O wins on the diagonal"
        return is_winner 

    #-----------------check for a reversed diagonal win-----------------
    xReversedDiagonal = False
    oReversedDiagonal = False
    #loop for x
    for x in range(rows):
        if board[x][columns - 1 - x] != 'X':
            is_winner = " "
            xReversedDiagonal = False
            break
        else:
            xReversedDiagonal = True
    if xReversedDiagonal == True:
        is_winner = "X wins on the reversed diagonal"
        return is_winner
    
    #loop for o
    for x in range(rows):
        if board[x][columns - 1 - x] != 'O':
            is_winner = " "
            oReversedDiagonal = False
            break
        else:
            oReversedDiagonal = True
    if oReversedDiagonal == True:
        is_winner = "O wins on the reversed diagonal"
        return is_winner
    

    #-----------------check for a cross win-----------------
    #vertical
    xVertical = False
    oVertical = False
    #loop for x
    for x in range(rows):
        if board[x][round(columns / 2)] != 'X':
            is_winner = " "
            xVertical = False
            break
        else:
            xVertical = True
    if xVertical == True:
        is_winner = "X wins on the cross"
        return is_winner
    
    #loop for o
    for x in range(rows):
        if board[x][round(columns / 2)] != 'O':
            is_winner = " "
            oVertical = False
            break
        else:
            oVertical = True
    if oVertical == True:
        is_winner = "O wins on the cross"
        return is_winner

    #horizontal
    xHorizontal = False
    oHorizontal = False
    #loop for x
    for x in range(columns):
        if board[round(rows / 2)][x] != 'X':
            is_winner = " "
            xHorizontal = False
            break
        else:
            xHorizontal = True
    if xHorizontal == True:
        is_winner = "X wins on the cross"
        return is_winner
    
    #loop for o
    for x in range(columns):
        if board[round(rows / 2)][x] != 'O':
            is_winner = " "
            oHorizontal = False
            break
        else:
            oHorizontal = True
    if oHorizontal == True:
        is_winner = "O wins on the cross"
        return is_winner

    return is_winner

"""
    - make use of the simulated board-game below to play the game
    - each time you test it is mandatory to first execute generate_board() 
      and secondly print_board(game_board) - this is provided to you for each test case
    - each test case is separate, clear the comments below for one test case, test it and 
      move on systematically
"""


   #play one move
   #message = "Move successfully played"
"""
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
game_board, message = place_row_col(game_board, "O", 2, 0)
game_board, message = place_row_col(game_board, "X", 0, 0)
game_board, message = place_row_col(game_board, "O", 2, 4)
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