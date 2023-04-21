from Animal import Animal


class Wolf(Animal):
    def __init__(self, strength, age, position_x, position_y, world):
        self.strength = strength
        if self.strength == 0:
            self.strength = 9
        super().__init__(self.strength, 5, age, position_x, position_y, world, "Wolf")

    def draw(self):
        return [(255, 100, 100), 'W']
