import random

from AlzurShield import AlzurShield
from Animal import Animal
from AntelopeSpeed import AntelopeSpeed
from Immortality import Immortality
from MagicalPotion import MagicalPotion
from Purification import Purification


class Human(Animal):
    def __init__(self, strength, age, position_x, position_y, world):
        self.strength = strength
        self.__specialAbility = None
        self.__abilities_cooldown = {"Immortality": 0, "MPotion": 0, "ASpeed": 0, "AShield": 0, "Purification": 0}
        self.__abilities_names = {"Immortality": Immortality, "MPotion": MagicalPotion, "ASpeed": AntelopeSpeed, "AShield": AlzurShield, "Purification": Purification}
        if self.strength == 0:
            self.strength = 5
        super().__init__(self.strength, 4, age, position_x, position_y, world, "Human")

    @property
    def specialAbility(self):
        return self.__specialAbility

    @specialAbility.setter
    def specialAbility(self, new_ability):
        self.__specialAbility = new_ability

    @property
    def abilities_cooldown(self):
        return self.__abilities_cooldown

    @abilities_cooldown.setter
    def abilities_cooldown(self, new_cd):
        self.__abilities_cooldown = new_cd

    @property
    def abilities_names(self):
        return self.__abilities_names

    @abilities_names.setter
    def abilities_names(self, new_n):
        self.__abilities_names = new_n

    def draw(self):
        return [(100, 0, 255), 'H']

    def action(self, organisms):
        for i in range(len(self.abilities_cooldown)):
            if self.abilities_cooldown[self.world.all_abilities_names[i]] != 0:
                self.abilities_cooldown[self.world.all_abilities_names[i]] -= 1
        if self.specialAbility is not None:
            if self.specialAbility.duration_left > 0:
                self.world.action_text.append(
                    self.specialAbility.giveName() + " " + str(self.specialAbility.duration_left - 1) + " turns left")
                self.specialAbility.duration_left -= 1
                if isinstance(self.specialAbility, MagicalPotion):
                    self.strength -= 1
                    self.world.action_text.append("strength: " + str(self.strength))
                elif isinstance(self.specialAbility, AntelopeSpeed):
                    if self.specialAbility.duration_left < 2:
                        rand = random.randint(1, 2)
                        if rand == 1:
                            self.compute_for_antelope()
                    else:
                        self.compute_for_antelope()
            else:
                self.world.action_text.append(self.specialAbility.giveName() + " ended")
                self.abilities_cooldown[self.specialAbility.giveName()] = 5
                self.specialAbility = None
        super().action(organisms)

    def collision(self, organism):
        if self.specialAbility is not None:
            if isinstance(self.specialAbility, Immortality):
                if self.name == organism.name:
                    x = self.free_pos_xy()[0]
                    y = self.free_pos_xy()[1]
                    if self.position_x != x or self.position_y != y:
                        self.position_x = x
                        self.position_y = y
                else:
                    if isinstance(organism, self.world.dictionary["Guarana"]):
                        self.strength += 3
                    if isinstance(organism, self.world.dictionary["Turtle"]) and self.strength < 5:
                        self.speedX = 0
                        self.speedY = 0
                        self.world.action_text.append("Turtle reflected attack!")
                    elif self.strength >= organism.strength:
                        self.world.remove_organism_next_turn(organism)
                    else:
                        self.world.action_text.append("Human survived!")
                        x = self.free_pos_xy()[0]
                        y = self.free_pos_xy()[1]
                        if self.position_x != x or self.position_y != y:
                            self.position_x = x
                            self.position_y = y
                return
            super().collision(organism)
            if isinstance(self.specialAbility, AlzurShield):
                if self.name == organism.name:
                    x = self.free_pos_xy()[0]
                    y = self.free_pos_xy()[1]
                    if self.position_x != x or self.position_y != y:
                        self.position_x = x
                        self.position_y = y
                else:
                    if isinstance(organism, self.world.dictionary["Guarana"]):
                        self.strength += 3
                    if isinstance(organism, self.world.dictionary["Turtle"]) and self.strength < 5:
                        self.speedX = 0
                        self.speedY = 0
                        self.world.action_text.append("Turtle reflected attack!")
                    elif self.strength >= organism.strength:
                        self.world.remove_organism_next_turn(organism)
                    else:
                        self.world.action_text.append("Human shielded!")
                        x = self.free_pos_xy()[0]
                        y = self.free_pos_xy()[1]
                        if organism.position_x != x or organism.position_y != y:
                            organism.position_x = x
                            organism.position_y = y
                return
            super().collision(organism)
            if isinstance(self.specialAbility, Purification):
                if self.world.gridWorld is True:
                    for i in self.world.organisms:
                        if i.position_y == self.position_y and (
                                i.position_x == self.position_x or i.position_x == self.position_x + 1 or i.position_x == self.position_x - 1):
                            self.world.remove_organism_next_turn(i)
                        elif i.position_x == self.position_x and (
                                i.position_y == self.position_y or i.position_y == self.position_y + 1 or i.position_y == self.position_y - 1):
                            self.world.remove_organism_next_turn(i)
                else:
                    for i in self.world.organisms:
                        if self.position_y % 2 == 1:
                            if i.position_x == self.position_x and (
                                    i.position_y == self.position_y or i.position_y == self.position_y - 1 or i.position_y == self.position_y + 1 or i.position_y == self.position_y + 2 or i.position_y == self.position_y - 2):
                                self.world.remove_organism_next_turn(i)
                            elif i.position_x == self.position_x + 1 and (
                                    i.position_y == self.position_y + 1 or i.position_y == self.position_y - 1):
                                self.world.remove_organism_next_turn(i)
                        else:
                            if i.position_x == self.position_x and (
                                    i.position_y == self.position_y or i.position_y == self.position_y - 1 or i.position_y == self.position_y + 1 or i.position_y == self.position_y + 2 or i.position_y == self.position_y - 2):
                                self.world.remove_organism_next_turn(i)
                            elif i.position_x == self.position_x - 1 and (
                                    i.position_y == self.position_y + 1 or i.position_y == self.position_y - 1):
                                self.world.remove_organism_next_turn(i)
                return
            super().collision(organism)
            return
        super().collision(organism)

    def compute_for_antelope(self):
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
