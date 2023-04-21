from Animal import Animal


class Sheep(Animal):
    def __init__(self, strength, age, position_x, position_y, world):
        self.strength = strength
        if self.strength == 0:
            self.strength = 4
        super().__init__(self.strength, 4, age, position_x, position_y, world, "Sheep")

    def draw(self):
        return [(150, 150, 150), 'S']
