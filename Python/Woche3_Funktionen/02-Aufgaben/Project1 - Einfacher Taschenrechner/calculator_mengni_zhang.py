"""
Einfacher Taschenrechner für mathematische Grundoperationen.
Führt Berechnungen mit zwei Zahlen durch und wiederholt auf Wunsch.
"""

import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "x": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod,
    "**": operator.pow,
}

print("===============================================")
print("Guten Tag!")
print("Ich bin der beste Taschenrechner!")
print("===============================================")

while True:
    num1 = float(input("Tippe die erste Zahl ein... "))
    operator = input("Was willst du mit dieser Zahl tun? ")
    num2 = float(input("Tippe die zweite Zahl ein... "))

    result = ops[operator](num1, num2)

    print("===============================================")
    print(f"Das Ergebnis der Rechnung {num1} {operator} {num2} lautet {result}!")
    print("===============================================")

    play_again = input("Noch einmal? (j/n) ").lower().strip()[0]

    if play_again != "y":
        break
