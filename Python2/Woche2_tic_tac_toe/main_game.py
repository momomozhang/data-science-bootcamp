from functions import (
    PLAYER_O,
    PLAYER_X,
    choose_square,
    display_board,
    is_full_board,
    player_order,
    replay,
    win_check,
)


def play_single_game():
    # Set up the data structure
    # Board is a 3x3 grid. it's data structure is a dictionary.
    # The dictionary keys are the name of 9 squares from A1 - C3.
    valid_cells = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

    # Before each square is taken, the square's name will be shown,
    # so it's easy for the players to choose.
    board = {cell: f"({cell})" for cell in valid_cells}

    game_on = True

    print()
    print("Yaaay! Let's play!")

    players = player_order()
    player_symbols = {players[0]: PLAYER_X, players[1]: PLAYER_O}
    turn = players[0]
    display_board(board)

    while game_on:
        if turn == players[0]:
            player_choice = choose_square(turn, board, valid_cells)
            board[player_choice] = PLAYER_X
            display_board(board)

            if win_check(board):
                game_on = False
                print(f"\n{turn} has won the game!")
            elif is_full_board(board):
                game_on = False
                print("\nBoard is full. It's a draw.")
            else:
                turn = players[1]
                print(f"\nNow it's {players[1]}'s turn.")

        else:
            player_choice = choose_square(turn, board, valid_cells)
            board[player_choice] = PLAYER_O
            display_board(board)

            if win_check(board):
                game_on = False
                print(f"\n{turn} has won the game!")
            elif is_full_board(board):
                game_on = False
                print("\nBoard is full. It's a draw.")
            else:
                turn = players[0]
                print(f"\nNow it's {players[0]}'s turn.")


def main():
    """Main game execution function"""

    play_game = ""

    print("Let's play Tic Tac Toe!")

    # print("Are you ready to play? Enter Yes or No")
    while play_game == "":
        play_game = input("Are you ready to play? Enter Yes or No: ").lower().strip()

    while play_game.startswith("y"):
        play_single_game()
        if replay():
            play_game = "y"
        else:
            play_game = "n"

    print("\nYou don't want to play again? Sad :(")


if __name__ == "__main__":
    main()
