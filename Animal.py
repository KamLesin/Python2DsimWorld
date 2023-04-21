from AlzurShield import AlzurShield
from Immortality import Immortality
from Organism import Organism


class Animal(Organism):

    def __init__(self, strength, initiative, age, position_x, position_y, world, name):
        super().__init__(strength, initiative, age, position_x, position_y, world, name)
        self.__speedX = 0
        self.__speedY = 0

    @property
    def speedX(self):
        return self.__speedX

    @speedX.setter
    def speedX(self, new_x):
        self.__speedX = new_x

    @property
    def speedY(self):
        return self.__speedY

    @speedY.setter
    def speedY(self, new_y):
        self.__speedY = new_y

    def action(self, organisms):
        self.age += 1
        for i in organisms:
            if i == self:
                continue
            if self.position_x + self.speedX == i.position_x and self.position_y + self.speedY == i.position_y:
                self.collision(i)
                if self.name == i.name:
                    self.speedX = 0
                    self.speedY = 0
                    return
        if self.position_x + self.speedX >= self.world.x or self.position_x + self.speedX < 0 or \
                self.position_y + self.speedY >= self.world.y or self.position_y + self.speedY < 0:
            self.speedX = 0
            self.speedY = 0
            return
        self.position_x = self.position_x + self.speedX
        self.position_y = self.position_y + self.speedY
        self.speedX = 0
        self.speedY = 0

    def collision(self, organism):
        if self.name == organism.name:
            x = self.free_pos_xy()[0]
            y = self.free_pos_xy()[1]
            if self.position_x != x or self.position_y != y:
                self.world.add_organism_next_turn(0, 0, x, y, self.name)
        else:
            if isinstance(organism, self.world.dictionary["Guarana"]):
                self.strength += 3
            elif isinstance(organism, self.world.dictionary["Turtle"]) and self.strength < 5:
                self.speedX = 0
                self.speedY = 0
                self.world.action_text.append("Turtle reflected attack!")
            elif self.strength >= organism.strength:
                if isinstance(organism, self.world.dictionary["Human"]) and isinstance(self.world.human.specialAbility,
                                                                                       Immortality):
                    self.world.action_text.append("Human survived!")
                    temp_x = organism.free_pos_xy()[0]
                    temp_y = organism.free_pos_xy()[1]
                    organism.position_x = temp_x
                    organism.position_y = temp_y
                    self.speedX = 0
                    self.speedY = 0
                    return
                self.world.remove_organism_next_turn(organism)
                organism.died = True
            else:
                if isinstance(organism, self.world.dictionary["Human"]) and isinstance(self.world.human.specialAbility,
                                                                                       AlzurShield):
                    self.world.action_text.append("Human shielded!")
                    x = self.free_pos_xy()[0]
                    y = self.free_pos_xy()[1]
                    if self.position_x != x or self.position_y != y:
                        self.position_x = x
                        self.position_y = y
                self.world.remove_organism_next_turn(self)
                self.died = True
