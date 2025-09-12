from random import randint

player_score = 0
computer_score = 0


def print_result():
    print(f"Aktueller Punktestand: Du: {player_score} vs. Computer: {computer_score}")


print("Willkommen zu Schere-Stein-Papier!")
print("Wähle: 1 für Stein, 2 für Schere, 3 für Papier, 0 zum Beenden")

while True:
    print("===============================================")
    print_result()

    player_choice = input("Deine Wahl (1=Stein, 2=Schere, 3=Papier, 0=Beenden): ")

    if player_choice not in ["0", "1", "2", "3"]:
        print("Ungültige Eingabe! Bitte wähle 0, 1, 2 oder 3.")
        continue

    player_choice = int(player_choice)

    if player_choice == 0:
        print("Spiel beendet!")
        print_result()
        if player_score > computer_score:
            print("Glückwunsch! Du hast gewonnen!")
        elif player_score < computer_score:
            print("Der Computer hat gewonnen!")
        else:
            print("Unentschieden!")
        break

    computer_choice = randint(1, 3)

    choice_text = {1: "Stein", 2: "Schere", 3: "Papier"}

    print(f"Du wählst: {choice_text[player_choice]}")
    print(f"Der Computer wählt: {choice_text[computer_choice]}")

    if player_choice == computer_choice:
        print("Unentschieden!")
    elif (
        (player_choice == 1 and computer_choice == 2)
        or (player_choice == 2 and computer_choice == 3)
        or (player_choice == 3 and computer_choice == 1)
    ):
        print("Du gewinnst diese Runde!")
        player_score += 1
    else:
        print("Computer gewinnt diese Runde!")
        computer_score += 1
