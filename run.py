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

input("\nPress Enter to start playing: ")

def print_board():
    """
       This function displays the current state of the board.
    """
    print("")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("")


def print_scoreboard():
    """
    This function prints a scoreboard of a game,
    showing the number of wins for the player and the computer,
    as well as the number of ties. The names of the player 
    and the computer are also displayed.

    """
    print("\nScoreboard: ")
    print(player_name + ": " + str(player_wins) + " wins")
    print("Computer: " + str(computer_wins) + " wins")
    print("Ties: " + str(ties) + "\n")

def computer_move(icon):
    """
    This function makes a move for the computer
     in the game. The computer plays randomly 
     choosing a position on the board that is currently 
     empty and marks it with the specified icon.
 
    """
    while True:
        choice = random.randint(0, 8)
        if board[choice] == ' ':
            board[choice] = icon
            break



while True:
    computer_move('O')
    print_board()
    breaks
    
    board = [' ' for x in range(9)]
        



ADD computer_move function for computer player's turn in the game
This function allows the computer player to make a 
move by randomly selecting an empty position on the
 game board and marking it with the specified icon. 
 The function ensures that the chosen position is valid by
  checking if it is empty before making the move.