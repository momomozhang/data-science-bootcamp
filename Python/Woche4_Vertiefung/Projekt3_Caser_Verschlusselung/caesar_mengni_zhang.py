"""
Cäsar-Verschlüsselung: Verschlüsselt Text durch Verschiebung der Buchstaben im Alphabet.
Eingabe: Text (nur Kleinbuchstaben) und Verschiebungszahl.
Ausgabe: Verschlüsselter Text.
"""


def encrypt_text(text: str, shift: int) -> str:
    new_text = ""
    for letter in text:
        if letter == " ":
            new_text += letter
        else:
            position = ord(letter) - ord("a")
            new_position = (position + shift) % 26
            new_letter = chr(ord("a") + new_position)
            new_text += new_letter
    return new_text.lower()


def decrypt_text(text: str, shift: int) -> str:
    original_text = ""
    for letter in text:
        if letter == " ":
            original_text += letter
        else:
            position = ord(letter) - ord("a")
            old_position = (position - shift) % 26
            old_letter = chr(ord("a") + old_position)
            original_text += old_letter
    return original_text.lower()


def main():
    while True:
        while True:
            encrypt_or_decrypt = input(
                "Wählen Sie 1 zum Verschlüsseln oder 2 zum Entschlüsseln: "
            ).strip()
            if encrypt_or_decrypt in ["1", "2"]:
                break
            print("Ungültige Eingabe, bitte noch einmal versuchen.")

        while True:
            text_input = input("Gib den Text ein: ").lower().strip()
            words = text_input.split(" ")
            all_alpha = all(word.isalpha() for word in words)
            if all_alpha:
                break
            print("Nur Buchstaben sind erlaubt, bitte noch einmal eingeben.")

        while True:
            shift_number = input("Wie viel ist die Verschiebung? ")
            if shift_number.isdigit():
                shift_number = int(shift_number)
                break
            print(
                "Die Verschiebung darf nur eine positive ganze Zahl sein. Bitte nochmal eingeben."
            )

        if encrypt_or_decrypt == "1":
            print(
                f"Der verschlüsselte Text von '{text_input}' mit {shift_number} Verschiebungen "
                f"ist '{encrypt_text(text_input, shift_number)}'."
            )
        else:
            print(
                f"Der entschlüsselte Originaltext von '{text_input}' mit {shift_number} "
                f"Verschiebungen ist '{decrypt_text(text_input, shift_number)}'."
            )

        repeat = input("Noch einmal? (j/n): ").lower().strip()

        if repeat[0] == "n":
            break


if __name__ == "__main__":
    main()
