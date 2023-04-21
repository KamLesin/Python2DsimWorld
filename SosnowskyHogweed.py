from CyberSheep import CyberSheep
from Plant import Plant


class SosnowskyHogweed(Plant):
    def __init__(self, strength, age, position_x, position_y, world):
        self.strength = strength
        if self.strength == 0:
            self.strength = 10
        super().__init__(self.strength, 0, position_x, position_y, world, "Hogweed")

    def draw(self):
        return [(51, 0, 102), 'N']

    def action(self, organisms):
        if self.world.gridWorld is True:
            for i in organisms:
                if isinstance(i, SosnowskyHogweed) or isinstance(i, CyberSheep):
                    continue
                elif i.position_y == self.position_y and (i.position_x == self.position_x or i.position_x == self.position_x + 1 or i.position_x == self.position_x - 1):
                    self.world.remove_organism_next_turn(i)
                elif i.position_x == self.position_x and (i.position_y == self.position_y or i.position_y == self.position_y + 1 or i.position_y == self.position_y - 1):
                    self.world.remove_organism_next_turn(i)
        else:
            for i in organisms:
                if self.position_y % 2 == 1:
                    if isinstance(i, SosnowskyHogweed) or isinstance(i, CyberSheep):
                        continue
                    elif i.position_x == self.position_x and (i.position_y == self.position_y or i.position_y == self.position_y - 1 or i.position_y == self.position_y + 1 or i.position_y == self.position_y + 2 or i.position_y == self.position_y - 2):
                        self.world.remove_organism_next_turn(i)
                    elif i.position_x == self.position_x + 1 and (i.position_y == self.position_y + 1 or i.position_y == self.position_y - 1):
                        self.world.remove_organism_next_turn(i)
                else:
                    if isinstance(i, SosnowskyHogweed) or isinstance(i, CyberSheep):
                        continue
                    elif i.position_x == self.position_x and (i.position_y == self.position_y or i.position_y == self.position_y - 1 or i.position_y == self.position_y + 1 or i.position_y == self.position_y + 2 or i.position_y == self.position_y - 2):
                        self.world.remove_organism_next_turn(i)
                    elif i.position_x == self.position_x - 1 and (i.position_y == self.position_y + 1 or i.position_y == self.position_y - 1):
                        self.world.remove_organism_next_turn(i)
        super().action(organisms)
