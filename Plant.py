import random

from Organism import Organism


class Plant(Organism):

    def __init__(self, strength, age, position_x, position_y, world, name):
        super().__init__(strength, 0, age, position_x, position_y, world, name)

    def action(self, organisms):
        self.age += 1
        rand = random.randint(1, 10)
        if rand == 1:
            self.sow()

    def collision(self, organism):
        pass

    def sow(self):
        x = self.free_pos_xy()[0]
        y = self.free_pos_xy()[1]
        if self.position_x != x or self.position_y != y:
            self.world.add_organism_next_turn(0, 0, x, y, self.name)
