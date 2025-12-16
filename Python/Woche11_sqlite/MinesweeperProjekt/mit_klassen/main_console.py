from world import World


def print_instructions():
    print("======================================================")
    print("Anweisungen:")
    print("1. Gib die Reihe und die Spalte an, z.B. '2 3'")
    print("2. Um eine Flage zu setzten, gib noch ein 'F' ein, z.B. '2 3 F'")


def create_world():
    try:
        print("Gib die Dimensionen ein oder drücke `Enter` um ein klassisches Spiel zu starten!")
        n_row = int(input("Gib die Anzahl an Zeilen  ein: "))
        n_col = int(input("Gib die Anzahl an Spalten ein: "))
        n_bombs = int(input("Gib die Anzahl an Bomben  ein: "))
        return World(n_row, n_col, n_bombs)
    except (ValueError, EOFError):
        return World()


def start():
    world = create_world()
    game_over = False

    while not game_over:
        print(world)
        print_instructions()

        try:
            user_input = input("\nGib die Reihe und die Spalte an: ").split()
            row, col = int(user_input[0]), int(user_input[1])
            assert row < world.height and col < world.width
        except (ValueError, IndexError, AssertionError):
            print("Falscher Input!")
            continue

        if len(user_input) == 3 and user_input[2].lower() == "f":
            world.set_flag(row, col)

        if len(user_input) == 2:
            world.open_field(row, col)

            if world[row, col].flag:
                continue

            if world[row, col].is_bomb():
                print("GAME OVER!!!")
                game_over = True
                print(world)

        if world.check_victory():
            print("Gewonnen!")
            game_over = True
            print(world)


while True:
    start()
    usr = input("Willst du nochmal spielen [j/n]\n").lower()

    if usr == "n":
        print("Auf Wiedersehen!")
        break
