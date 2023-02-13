import random

player_name = input("Enter your name: ").strip()
board = [' ' for x in range(9)]

player_wins = 0
computer_wins = 0
ties = 0

print("\nWelcome to Tic-Tac-Toe, " + player_name + "!\n")
print("The rules of the game are as follows:\n")
print("1. The game is played on a 3x3 grid.")
print("2. You will be 'X' and the computer will be 'O'.")
print("3. To make a move, enter a number from 1 to 9.")
print("4. The numbers correspond to the positions on the grid as follows:\n")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")
print("\n5. The first player to get three of their \nsymbols in a row ")
print("horizontally, vertically, or diagonally) wins the game.")
print("6. If all the cells on the grid are filled and ")
print("no player has won, the game ends in a draw.")


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







