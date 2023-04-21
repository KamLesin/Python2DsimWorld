from Plant import Plant


class SowThistle(Plant):
    def __init__(self, strength, age, position_x, position_y, world):
        super().__init__(0, 0, position_x, position_y, world, "SowThistle")

    def draw(self):
        return [(255, 255, 153), 'T']

    def action(self, organisms):
        for i in range(3):
            super().action(organisms)
