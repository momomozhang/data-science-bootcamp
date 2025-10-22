import logging
import re

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def check_email(input_email: str) -> str:
    """Die Funktion checkt, ob der String ‘input_email‘ eine valide Adresse darstellt.

    Parameters:
    input_email (str)

    Returns:
    str
    """
    input_email = input_email.strip()
    assert isinstance(input_email, str)
    assert len(input_email) >= 0
    pattern = r"^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$"
    assert re.fullmatch(pattern, input_email)

    return input_email


def check_age(input_age: str) -> int:
    """Die Funktion checkt, ob der String ‘input_age‘ ein valides Alter darstellt.

    Parameters:
    input_age (str)

    Returns:
    int
    """
    input_age = input_age.strip()
    assert isinstance(int(input_age), int)
    age = int(input_age)
    assert age >= 0 and age <= 150
    return age


def main():
    input_text = ""
    while input_text != "q":
        print("")
        print("Drücke '?' um Hilfe zu bekommen.")
        print("Drücke 'q' um die App zu verlassen.")
        print("Drücke 'w' um weiterzumachen.")
        print("")
        input_text = input().strip()
        if input_text == "?":
            print("check_email:")
            print(check_email.__doc__)
            print("")
            print("check_age:")
            print(check_age.__doc__)

        elif input_text == "w":
            input_str = input("Wie lautet deine Email? \n")
            print("")
            logging.debug(f"Eingegebene Email ist {input_str}.")
            logging.info("Funktion 'check_email' wurde aufgerufen.")
            try:
                check_email(input_str)
            except (AssertionError, ValueError):
                logging.error("Bitte gib eine korrekte Email an!")
                continue

            print("")
            input_str = input("Wie alt bist du? \n")
            print("")
            logging.debug(f"Eingegebenes Alter ist {input_str}.")
            logging.info("Funktion 'check_age' wurde aufgerufen.")
            try:
                check_age(input_str)
            except (AssertionError, ValueError):
                logging.error("Bitte gib ein korrektes Alter an!")
                continue
        else:
            logging.error("Bitte gib einen korrekten Input an!")

    logging.debug("Die Schleife wurde beendet.")


if __name__ == "__main__":
    main()
