import random

player_name = input("Enter your name: ").strip()
board = [' ' for x in range(9)]

def print_board():
    """
       This function displays the current state of the grid.
    """
    print("")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("")

print_board()   





