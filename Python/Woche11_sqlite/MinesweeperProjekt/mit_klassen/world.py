import random

from tile import Tile


class World:
    def __init__(self, height=8, width=8, bombs=15):
        self.height = height
        self.width = width
        self.bombs = bombs
        self.number_of_flags = 0

        self.generate_board_with_bombs(self.bombs)
        self.generate_values()

    def open_field(self, row, col):
        if not self[row, col].opened and not self[row, col].flag:
            self[row, col].open_field()
            self.opened_fields += 1

    def set_flag(self, row, col):
        if self[row, col].flag:
            self[row, col].unset_flag()
            self.number_of_flags -= 1
        else:
            self[row, col].set_flag()
            self.number_of_flags += 1

    def generate_board_with_bombs(self, number_of_bombs):
        self.opened_fields = 0
        self.number_of_flags = 0
        self.data = []

        for _ in range(self.height):
            row = [Tile() for _ in range(self.width)]
            self.data.append(row)

        total_cells = self.width * self.height
        bombs = random.sample(range(total_cells), number_of_bombs)

        for b in bombs:
            row = b // self.width
            col = b % self.width
            self[row, col] = Tile("Bomb")

    def generate_values(self):
        for row in range(self.height):
            for col in range(self.width):
                if self[row, col].type == "Bomb":
                    continue

                if row > 0 and self[row - 1, col].type == "Bomb":
                    self[row, col].value += 1

                if row < self.height - 1 and self[row + 1, col].type == "Bomb":
                    self[row, col].value += 1

                if col > 0 and self[row, col - 1].type == "Bomb":
                    self[row, col].value += 1

                if col < self.width - 1 and self[row, col + 1].type == "Bomb":
                    self[row, col].value += 1

                if col > 0 and row > 0 and self[row - 1, col - 1].type == "Bomb":
                    self[row, col].value += 1

                if col > 0 and row < self.height - 1 and self[row + 1, col - 1].type == "Bomb":
                    self[row, col].value += 1

                if col < self.width - 1 and row > 0 and self[row - 1, col + 1].type == "Bomb":
                    self[row, col].value += 1

                if (
                    col < self.width - 1
                    and row < self.height - 1
                    and self[row + 1, col + 1].type == "Bomb"
                ):
                    self[row, col].value += 1

    def check_victory(self):
        total_cells = self.width * self.height
        return self.opened_fields == total_cells - self.bombs

    def __setitem__(self, point, value):
        row, col = point
        self.data[row][col] = value

    def __getitem__(self, point):
        row, col = point
        return self.data[row][col]

    def __repr__(self):
        s = "\n\t\t\tMINESWEEPER\n"

        col_header = "    "
        hline = "   |"

        for c in range(self.width):
            col_header += f"{c:^6}"
            hline += "-----|"

        s += col_header + "\n"

        for row in range(self.height):
            s += hline + "\n"
            str_row = ""

            for col in range(self.width):
                symbol = self[row, col].__repr__()

                if symbol in ("💣", "🚩"):
                    str_row += f"{symbol:^4}|"
                else:
                    str_row += f"{symbol:^5}|"

            s += f" {row} |{str_row}\n"

        s += hline
        s += f"\n\nGesetzte Flaggen: {self.number_of_flags}\n"
        s += f"Geöffnete Felder: {self.opened_fields}\n"

        return s
