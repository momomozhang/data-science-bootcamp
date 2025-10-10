class Tier:
    def __init__(self, name: str, sex: bool, age: int | float):
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self) -> str:
        return f"{self.name} isst."

    def sleep(self) -> str:
        return f"{self.name} schläft."

    def grow(self, years: int | float) -> str:
        self.age += years
        return f"{self.name} wurde {years} Jahre älter und ist jetzt {self.age} Jahre alt."

    def show_sex(self):
        if self.sex == 0:
            return f"{self.name} ist ein gutes Mädchen."
        return f"{self.name} ist ein Junge."
