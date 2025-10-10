from tier import Tier


class Tiger(Tier):
    # class attributes
    num_appendages = 4
    is_cold_blooded = False
    is_mammal = True

    def __init__(self, name: str, sex: bool, age: int | float, danger: bool):
        super().__init__(name, sex, age)
        self.danger = danger

    def eat(self):
        return f"Vorsicht! Tiger {self.name} kann vielleicht dich essen!"

    def sleep(self):
        return f"Tiger {self.name} jetzt schläft. Aber {self.name} ist noch sehr gefährlich."

    def show_sex(self):
        if self.sex == 0:
            return f"{self.name} ist eine tödliche Königin!"
        return f"{self.name} ist ein gefährlicher Typ!"

    def scary_children(self, num: int):
        return (
            f"Tiger {self.name} hat schon {num} Kinder gegessen. "
            f"Denn sie machten ihre Hausaufgaben nicht."
        )

    def is_danger(self):
        if self.danger == 1:
            answer = "Definitiv!"
        answer = "Mag sein!"
        return f"Ist {self.name} richtig gefährlich? {answer}"
