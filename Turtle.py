from Animal import Animal
import random


class Turtle(Animal):
    def __init__(self, strength, age, position_x, position_y, world):
        self.strength = strength
        if self.strength == 0:
            self.strength = 2
        super().__init__(self.strength, 1, age, position_x, position_y, world, "Turtle")

    def draw(self):
        return [(0, 153, 76), 'T']

    def action(self, organisms):
        rand = random.randint(1, 4)
        if rand == 1:
            super().action(organisms)
