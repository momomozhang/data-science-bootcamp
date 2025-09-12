import random
import statistics


def roll_dice(n: int = 1) -> list[int]:
    roll_result = []
    for _ in range(1, n + 1):
        roll_result.append(random.randint(1, 6))
    return roll_result


def average_roll_numbers(n: int = 1) -> float:
    average = statistics.mean(roll_dice(n))
    return average


for i in [2, 4, 6, 8, 10, 100, 1000, 10000, 100000, 100000, 1000000]:
    print(f"Wenn n={i} ist, beträgt der berechnete Mittelwert {average_roll_numbers(i)}.")


# Je größer die Stichprobe ist, desto näher kommt das Ergebnis dem erwarteten Durchschnitt.
# Andererseits ist es bei kleineren Stichproben wahrscheinlicher,
# dass sie weit vom wahren Mittelwert entfernt sind.
# Deshalb sollten wir als Analysten vorsichtig sein,
# wenn wir Schlüsse aus kleinen Stichproben ziehen.
