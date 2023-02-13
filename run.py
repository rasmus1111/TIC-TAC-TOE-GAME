import random
import sys

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


def player_move(icon):
    """

    This function lets the player select a board position
    (1-9) and marks it with their icon. The function checks
    if the choice is valid and empty. If not, an error message 
    is shown and player must try again.

    :param icon: The icon used to mark the board position.
    :return: None
    """
    while True: 
        try:
            choice = input("To leave the game type 'exit' \n\nEnter your move (1-9): ").strip()
            if choice == 'exit':
                print("Thanks for playing Tic-Tac-Toe! Have a great day.")
                sys.exit()
            else:
                choice = int(choice) - 1
                if choice >= 0 and choice <= 8:
                    if board[choice] == ' ':
                        board[choice] = icon
                        break
                    else:
                        print("\nSpace already taken, try again.")
                else:
                    print("\nInvalid choice, try again.")
        except ValueError:
            print("\nInvalid input, try again.")

def check_victory(icon):
    """
    This function checks if the player or computer has won the game.
    Looks at all possible win combinations and returns True 
    if player has their icon in all positions of a row, column, or diagonal.
    
    """
    for i in range(3):
        if board[i*3] == icon and board[i*3 + 1] == icon and board[i*3 + 2] == icon:
            return True
        if board[i] == icon and board[i + 3] == icon and board[i + 6] == icon:
            return True
    if board[0] == icon and board[4] == icon and board[8] == icon:
        return True
    if board[2] == icon and board[4] == icon and board[6] == icon:
        return True
    return False


def check_draw():
    """
    this function checks if the game is a draw 
    and returns True if all positions filled.
    """
    for i in range(9):
        if board[i] == ' ':
            return False
    return True


while True:

    print_board()
    print_scoreboard()
    player_move('X')
    if check_victory('X'):
        print_board()
        print("X wins! Congratulations " + player_name + "!")
        player_wins += 1
        board = [' ' for x in range(9)]
    elif check_draw():
        print_board()
        print("It's a draw")
        ties += 1
        board = [' ' for x in range(9)]
    else:
        computer_move('O')
        if check_victory('O'):
            print_board()
            print("O wins! Better luck next time " + player_name + ".")
            computer_wins += 1
            board = [' ' for x in range(9)]



