import random


def print_board(board):
    n = len(board[0])
    print("\n\t\t\tMINESWEEPER\n")

    col_header = "    "
    hline = "   |"

    for c in range(n):
        col_header += f" {c:^4} "
        hline += "-----|"

    print(col_header)

    for r in range(n):
        print(hline)
        row = ""
        for c in range(n):
            if board[r][c] in ("💣", "🚩"):
                row += f"{board[r][c]:^4}|"
            else:
                row += f"{board[r][c]:^5}|"
        print(f" {r} |{row}")

    print(hline)


def print_instructions():
    print("Anweisungen:")
    print("1. Gib die Reihe und die Spalte an, z.B. '2 3'")
    print("2. Um eine Flage zu setzten, gib noch ein 'F' ein, z.B. '2 3 F'")


def check_victory(b, real_values, displayed_values):
    n = len(real_values[0])
    count = 0

    for r in range(n):
        for c in range(n):
            if displayed_values[r][c] != " " and displayed_values[r][c] != "🚩":
                count += 1

    return count == n * n - b


def generate_board_with_bombs(n, b):
    cells = [0 for i in range(n * n)]

    for i in range(b):
        cells[i] = "💣"

    random.shuffle(cells)

    board = [[" " for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            board[i][j] = cells[i + j * n]

    return board


def generate_values(board):
    n = len(board[0])

    for row in range(n):
        for col in range(n):
            if board[row][col] == "💣":
                continue

            if row > 0 and board[row - 1][col] == "💣":
                board[row][col] += 1

            if row > 0 and col > 0 and board[row - 1][col - 1] == "💣":
                board[row][col] += 1

            if row > 0 and col < n - 1 and board[row - 1][col + 1] == "💣":
                board[row][col] += 1

            if row < n - 1 and board[row + 1][col] == "💣":
                board[row][col] += 1

            if row < n - 1 and col > 0 and board[row + 1][col - 1] == "💣":
                board[row][col] += 1

            if row < n - 1 and col < n - 1 and board[row + 1][col + 1] == "💣":
                board[row][col] += 1

            if col > 0 and board[row][col - 1] == "💣":
                board[row][col] += 1

            if col < n - 1 and board[row][col + 1] == "💣":
                board[row][col] += 1

    return board


def start():
    n = 6
    b = 8
    flags = []

    real_values = []
    displayed_values = [[" " for y in range(n)] for x in range(n)]

    real_values = generate_board_with_bombs(n, b)
    real_values = generate_values(real_values)

    print_instructions()

    game_over = False
    while not game_over:
        print_board(displayed_values)

        try:
            inp = input("\nGib die Reihe und die Spalte an: ").split()
            r, c = int(inp[0]), int(inp[1])

            assert 0 <= r < n and 0 <= c < n
            assert displayed_values[r][c] == " " or displayed_values[r][c] == "🚩"

            if len(inp) == 3:
                assert inp[2].lower() == "f"
        except (ValueError, IndexError, AssertionError):
            print("Falscher Input! Versuche es nochmal!\n")
            print_instructions()
            continue

        if len(inp) == 3:
            if (r, c) not in flags:
                flags.append((r, c))
                displayed_values[r][c] = "🚩"
                print(f"Flag {(r, c)} hinzugefügt!")
            else:
                flags.remove((r, c))
                displayed_values[r][c] = " "
                print(f"Flag {(r, c)} wurde entfernt!")

        elif real_values[r][c] == "💣":
            displayed_values[r][c] = "💣"
            print_board(displayed_values)
            print("GAME OVER!!!")
            game_over = True

        else:
            displayed_values[r][c] = real_values[r][c]

        if check_victory(b, real_values, displayed_values):
            print_board(displayed_values)
            print("Du hast gewonnen!!!")
            game_over = True


start()
