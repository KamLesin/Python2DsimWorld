from Plant import Plant


class Grass(Plant):
    def __init__(self, strength, age, position_x, position_y, world):
        super().__init__(0, 0, position_x, position_y, world, "Grass")

    def draw(self):
        return [(0, 255, 0), 'g']
