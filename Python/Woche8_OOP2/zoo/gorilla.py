from tier import Tier


class Gorilla(Tier):
    # class attributes
    num_appendages = 4
    is_cold_blooded = False
    is_mammal = True

    def eat(self) -> str:
        return f"Gorilla {self.name} isst Bananen."

    def sleep(self) -> str:
        return f"Gorilla {self.name} schläft im Baum."

    def klettern(self) -> str:
        return f"Gorilla {self.name} klettert auf einen Baum."
