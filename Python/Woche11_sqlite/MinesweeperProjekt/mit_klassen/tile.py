class Tile:
    def __init__(self, tile_type="Number"):
        self.type = tile_type
        self.flag = False
        self.opened = False

        if tile_type == "Number":
            self.value = 0
        elif tile_type == "Bomb":
            self.symbol = "💣"

    def is_bomb(self):
        return self.type == "Bomb"

    def open_field(self):
        self.opened = True

    def set_flag(self):
        self.flag = True
        self.symbol = "🚩"

    def unset_flag(self):
        self.flag = False

    def __repr__(self):
        if self.flag:
            return self.symbol
        if not self.opened:
            return "?"
        if self.opened and self.type == "Number":
            return str(self.value)
        if self.opened and self.type == "Bomb":
            return self.symbol
        return ""
