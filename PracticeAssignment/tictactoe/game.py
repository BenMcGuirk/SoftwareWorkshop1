"""
Create a Tic Tac Toe game on the terminal. The game is played between two players. 
The first player is assigned the symbol 'X' and the second player is assigned the symbol 'O'.
The game is played on a 3x3 grid. The first player to get 3 of their symbols in a row (up, down, across, or diagonally) is the 
winner. When all 9 squares are full, the game is over. If no player has 3 symbols in a row, the game ends in a tie.
"""

import os
import random

class TicTacToe:
    """
    Tic Tac Toe game class
    """
    def __init__(self):
        self.board = [' '] * 10
        self.player1 = 'X'
        self.player2 = 'O'
        self.current_player = self.player1
        self.winner = None
        self.game_over = False
        self.moves = 0
        self.winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9], # horizontal
            [1, 4, 7], [2, 5, 8], [3, 6, 9], # vertical
            [1, 5, 9], [3, 5, 7] # diagonal
        ]

    def clear_screen(self):
        """
        Clear the terminal screen
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_board(self):
        """
        Display the board
        """
        self.clear_screen()
        print('  {} | {} | {}'.format(self.board[1], self.board[2], self.board[3]))
        print(' ---+---+---')
        print('  {} | {} | {}'.format(self.board[4], self.board[5], self.board[6]))
        print(' ---+---+---')
        print('  {} | {} | {}'.format(self.board[7], self.board[8], self.board[9]))

    def get_player_move(self):
        """
        Get the player's move
        """
        while True:
            try:
                move = int(input('Enter a number between 1 and 9: '))
                if move < 1 or move > 9:
                    raise ValueError
                if self.board[move] != ' ':
                    raise ValueError
                break
            except ValueError:
                print('Invalid move. Try again.')
        return move

    def get_computer_move(self):
        """
        Get the computer's move
        """
        while True:
            move = random.randint(1, 9)
            if self.board[move] == ' ':
                break
        return move

    def make_move(self, move):
        """
        Make a move
        """
        self.board[move] = self.current_player
        self.moves += 1

    def check_winner(self):
        """
        Check if there is a winner
        """
        for combination in self.winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                self.winner = self.current_player
                self.game_over = True
                break
        if self.moves == 9:
            self.game_over = True

    def switch_player(self):
        """
        Switch player
        """
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play(self):
        """
        Play the game
        """
        while not self.game_over:
            self.display_board()
            if self.current_player == self.player1:
                move = self.get_player_move()
            else:
                move = self.get_computer_move()
            self.make_move(move)
            self.check_winner()
            self.switch_player()
        self.display_board()
        if self.winner:
            print('The winner is {}'.format(self.winner))
        else:
            print('The game is a tie')

def main():
    """
    Main function
    """
    game = TicTacToe()
    game.play()

if __name__ == '__main__':
    main()