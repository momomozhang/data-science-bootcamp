"""
Tic-Tac-Toe Game

A simple implementation of the classic Tic-Tac-Toe game with a command-line interface.
Players take turns marking X and O on a 3x3 grid, aiming to get three of their marks in a row.
"""

import random

# Set up the data structure
# Board is a 3x3 grid. it's data structure is a dictionary.
# The dictionary keys are the name of 9 squares from A1 - C3.
valid_cells = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

# Before each square is taken, the square's name will be shown, so it's easy for the players to choose.
board = {cell: f"({cell})" for cell in valid_cells}


def display_board(board):
    """Display the board, update it according to players' choices"""
    print("\n" + "=" * 30 + "\n")
    print(board["A1"] + " | " + board["A2"] + " | " + board["A3"])
    print("__________________")
    print(board["B1"] + " | " + board["B2"] + " | " + board["B3"])
    print("__________________")
    print(board["C1"] + " | " + board["C2"] + " | " + board["C3"])


def player_order():
    """Automatically decide the player order."""
    print("Now enter both your names!")

    # get users' names
    player_a = input("Enter the first name: ")
    player_b = input("Enter the second name: ")
    print(f"We have {player_a} and {player_b}!")

    # draw the random order
    players = [player_a, player_b]
    random.shuffle(players)

    # print the player order
    print(f"{players[0]} goes first!")
    return players


def choose_square(player, board):
    """Take players' input to choose squares, then update the board and check if win / draw"""
    global valid_cells  # Access the global variable
    while True:
        player_choice = input(f"{player}, choose a square ").upper()

        if player_choice not in valid_cells:
            print(f"\n{player}, {player_choice} is not a valid square. Please choose again!")
            continue

        elif board[player_choice] == " X " or board[player_choice] == " O ":
            print(f"\n{player}, {player_choice} is already taken. Choose an empty square")
            continue

        else:
            print(f"\n{player} selected square: {player_choice}")
            return player_choice


def win_check(board):
    """Check if the game is won."""
    # Define all possible winning combinations
    combinations = [
        # Rows
        ["A1", "A2", "A3"],
        ["B1", "B2", "B3"],
        ["C1", "C2", "C3"],
        # Columns
        ["A1", "B1", "C1"],
        ["A2", "B2", "C2"],
        ["A3", "B3", "C3"],
        # Diagonals
        ["A1", "B2", "C3"],
        ["C1", "B2", "A3"],
    ]

    # Check each combination
    for keys in combinations:
        values = [board[key] for key in keys]
        if values[0] in [" X ", " O "] and all(value == values[0] for value in values):
            return True

    return False


def if_full_board(board):
    """Check if the board is already full"""
    for value in board.values():
        if value not in [" X ", " O "]:
            return False
    return True


def replay():
    """Ask if the user wants to play again"""
    response = input("Do you want to play again? Enter Yes or No: ").lower()
    if response.startswith("y"):
        return True
    else:
        print("\nYou don't want to play again? Sad :(")
        return False
