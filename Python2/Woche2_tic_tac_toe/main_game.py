from functions import *

# Set up the data structure
# Board is a 3x3 grid. it's data structure is a dictionary.
# The dictionary keys are the name of 9 squares from A1 - C3.
valid_cells = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

# Before each square is taken, the square's name will be shown, so it's easy for the players to choose.
board = {cell: f"({cell})" for cell in valid_cells}

play_game = ""

print("Let's play Tic Tac Toe!")

while True:
    game_on = False

    # print("Are you ready to play? Enter Yes or No")
    if play_game == "":
        play_game = input("Are you ready to play? Enter Yes or No: ")
    else:
        play_game = "yes"

    while play_game.lower().startswith("y"):
        game_on = True
        print("Yaaay! Let's play!")

        players = player_order()
        turn = players[0]
        display_board(board)

        while game_on:
            if turn == players[0]:
                player_choice = choose_square(turn, board)
                board[player_choice] = " X "
                display_board(board)

                if win_check(board):
                    game_on = False
                    print(f"\n{turn} has won the game!")
                elif if_full_board(board):
                    game_on = False
                    print("\nBoard is full. It's a draw.")
                else:
                    turn = players[1]
                    print(f"\nNow it's {players[1]}'s turn.")

            else:
                player_choice = choose_square(turn, board)
                board[player_choice] = " O "
                display_board(board)

                if win_check(board):
                    game_on = False
                    print(f"\n{turn} has won the game!")
                elif if_full_board(board):
                    game_on = False
                    print("\nBoard is full. It's a draw.")
                else:
                    turn = players[0]
                    print(f"\nNow it's {players[0]}'s turn.")

        if replay():
            # play_game = "yes"
            board = {cell: f"({cell})" for cell in valid_cells}
        else:
            play_game = False
            break

    else:
        print("\nYou don't want to play? Sad :(")
        game_on = False
    break
