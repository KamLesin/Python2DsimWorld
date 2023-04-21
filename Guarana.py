from Plant import Plant


class Guarana(Plant):
    def __init__(self, strength, age, position_x, position_y, world):
        super().__init__(0, 0, position_x, position_y, world, "Guarana")

    def draw(self):
        return [(255, 10, 10), 'G']
