from Plant import Plant


class Belladona(Plant):
    def __init__(self, strength, age, position_x, position_y, world):
        self.strength = strength
        if self.strength == 0:
            self.strength = 99
        super().__init__(self.strength, 0, position_x, position_y, world, "Belladona")

    def draw(self):
        return [(57, 5, 142), 'B']
