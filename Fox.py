from Animal import Animal


class Fox(Animal):
    def __init__(self,strength, age, position_x, position_y, world):
        self.strength = strength
        if self.strength == 0:
            self.strength = 3
        super().__init__(self.strength, 7, age, position_x, position_y, world, "Fox")

    def draw(self):
        return [(255, 128, 0), 'F']

    def action(self, organisms):
        for i in organisms:
            if self.position_x + self.speedX == i.position_x and self.position_y + self.speedY == i.position_y and self.strength < i.strength:
                return
        super().action(organisms)
