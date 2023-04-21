import random

from Animal import Animal


class Antelope(Animal):
    def __init__(self, strength, age, position_x, position_y, world):
        self.strength = strength
        if self.strength == 0:
            self.strength = 4
        super().__init__(self.strength, 4, age, position_x, position_y, world, "Antelope")

    def draw(self):
        return [(255, 255, 0), 'A']

    def action(self, organisms):
        if self.world.gridWorld is True:
            if self.speedX != 0:
                self.speedX *= 2
            if self.speedY != 0:
                self.speedY *= 2
        else:
            if (self.speedY > 1 or self.speedY < -1) and self.speedX == 0:
                self.speedY *= 2
            if self.position_y % 2 == 1:
                if self.speedY == -1 and self.speedX == 0:
                    self.speedY = -2
                    self.speedX = -1
                elif self.speedY == -1 and self.speedX == 1:
                    self.speedY = -2
                elif self.speedY == 1 and self.speedX == 0:
                    self.speedY = 2
                    self.speedX = -1
                elif self.speedY == 1 and self.speedX == 1:
                    self.speedY = 2
            else:
                if self.speedY == -1 and self.speedX == -1:
                    self.speedY = -2
                elif self.speedY == -1 and self.speedX == 0:
                    self.speedY = -2
                    self.speedX = 1
                elif self.speedY == 1 and self.speedX == -1:
                    self.speedY = 2
                elif self.speedY == 1 and self.speedX == 0:
                    self.speedY = 2
                    self.speedX = 1
        super().action(organisms)

    def collision(self, organism):
        rand = random.randint(1, 2)
        if rand > 0 and organism.name != self.name:
            x = organism.free_pos_xy()[0]
            y = organism.free_pos_xy()[1]
            if organism.position_x != x or organism.position_y != y:
                self.position_y = y
                self.position_x = x
                self.world.action_text.append("Antelope fled!")
                return
        super().collision(organism)
