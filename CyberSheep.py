from Animal import Animal
import math

class CyberSheep(Animal):
    def __init__(self, strength, age, position_x, position_y, world):
        self.strength = strength
        if self.strength == 0:
            self.strength = 11
        super().__init__(self.strength, 4, age, position_x, position_y, world, "CyberSheep")

    def draw(self):
        return [(255, 0, 255), 'C']

    def action(self, organisms):
        organism = None
        for i in organisms:
            if isinstance(i, self.world.dictionary["Hogweed"]):
                organism = i
                break
        if organism is not None:
            self.age += 1
            self.speedY = 0
            self.speedX = 0
            for i in organisms:
                if isinstance(i, self.world.dictionary["Hogweed"]) and self.is_closer(organism.position_x, organism.position_y, i.position_x, i.position_y):
                    organism = i
            self.change_pos(organism.position_x, organism.position_y, organism)
            return
        super().action(organisms)

    def change_pos(self, x, y, organism):
        if self.world.gridWorld is True:
            if self.position_x == x:
                if self.position_y > y:
                    self.position_y -= 1
                    if self.position_y == y and self.position_x == x:
                        self.collision(organism)
                elif self.position_y < y:
                    self.position_y += 1
                    if self.position_y == y and self.position_x == x:
                        self.collision(organism)
            elif self.position_y == y:
                if self.position_x > x:
                    self.position_x -= 1
                    if self.position_y == y and self.position_x == x:
                        self.collision(organism)
                elif self.position_x < x:
                    self.position_x += 1
                    if self.position_y == y and self.position_x == x:
                        self.collision(organism)
            elif self.position_x > x:
                self.position_x -= 1
                if self.position_y == y and self.position_x == x:
                    self.collision(organism)
            elif self.position_x < x:
                self.position_x += 1
                if self.position_y == y and self.position_x == x:
                    self.collision(organism)
            elif self.position_y > y:
                self.position_y -= 1
                if self.position_y == y and self.position_x == x:
                    self.collision(organism)
            elif self.position_y < y:
                self.position_y += 1
                if self.position_y == y and self.position_x == x:
                    self.collision(organism)
        else:
            if self.position_y % 2 == 0 and x == self.position_x and y % 2 == 0:
                if y > self.position_y:
                    self.position_y += 2
                    if self.position_y == y and self.position_x == x:
                        self.collision(organism)
                elif y < self.position_y:
                    self.position_y -= 2
                    if self.position_y == y and self.position_x == x:
                        self.collision(organism)
            elif self.position_y % 2 != y % 2 and x == self.position_x:
                if y > self.position_y:
                    self.position_y += 1
                    if self.position_y == y and self.position_x == x:
                        self.collision(organism)
                elif y < self.position_y:
                    self.position_y -= 1
                    if self.position_y == y and self.position_x == x:
                        self.collision(organism)
            elif self.position_y % 2 == 0:
                if x < self.position_x:
                    if y < self.position_y:
                        self.position_x -= 1
                        self.position_y -= 1
                        if self.position_y == y and self.position_x == x:
                            self.collision(organism)
                    elif y > self.position_y:
                        self.position_x -= 1
                        self.position_y += 1
                        if self.position_y == y and self.position_x == x:
                            self.collision(organism)
                    elif y == self.position_y:
                        if self.position_y + 1 < self.world.y:
                            self.position_x -= 1
                            self.position_y += 1
                            if self.position_y == y and self.position_x == x:
                                self.collision(organism)
                        else:
                            self.position_x -= 1
                            self.position_y -= 1
                            if self.position_y == y and self.position_x == x:
                                self.collision(organism)
                if x > self.position_x:
                    if y < self.position_y:
                        self.position_y -= 1
                        if self.position_y == y and self.position_x == x:
                            self.collision(organism)
                    elif y > self.position_y:
                        self.position_y += 1
                        if self.position_y == y and self.position_x == x:
                            self.collision(organism)
                    elif y == self.position_y:
                        if self.position_y + 1 < self.world.y:
                            self.position_y += 1
                            if self.position_y == y and self.position_x == x:
                                self.collision(organism)
                        else:
                            self.position_y -= 1
                            if self.position_y == y and self.position_x == x:
                                self.collision(organism)
            else:
                if x > self.position_x:
                    if y < self.position_y:
                        self.position_x += 1
                        self.position_y -= 1
                        if self.position_y == y and self.position_x == x:
                            self.collision(organism)
                    elif y > self.position_y:
                        self.position_x += 1
                        self.position_y += 1
                        if self.position_y == y and self.position_x == x:
                            self.collision(organism)
                    elif y == self.position_y:
                        if self.position_y + 1 < self.world.y:
                            self.position_x += 1
                            self.position_y += 1
                            if self.position_y == y and self.position_x == x:
                                self.collision(organism)
                        else:
                            self.position_x += 1
                            self.position_y -= 1
                            if self.position_y == y and self.position_x == x:
                                self.collision(organism)
                if x < self.position_x:
                    if y < self.position_y:
                        self.position_y -= 1
                        if self.position_y == y and self.position_x == x:
                            self.collision(organism)
                    elif y > self.position_y:
                        self.position_y += 1
                        if self.position_y == y and self.position_x == x:
                            self.collision(organism)
                    elif y == self.position_y:
                        if self.position_y + 1 < self.world.y:
                            self.position_y += 1
                            if self.position_y == y and self.position_x == x:
                                self.collision(organism)
                        else:
                            self.position_y -= 1
                            if self.position_y == y and self.position_x == x:
                                self.collision(organism)

    def is_closer(self, x1, y1, x2, y2):
        if self.world.gridWorld is True:
            if abs(self.position_x - x1) + abs(self.position_y - y1) > abs(self.position_x - x2) + abs(self.position_y - y2):
                return True
            return False
        else:
            var1 = int(math.sqrt(math.pow(self.position_x - x1, 2) + math.pow(self.position_y - y1, 2)))
            var2 = int(math.sqrt(math.pow(self.position_x - x2, 2) + math.pow(self.position_y - y2, 2)))
            if var1 >= var2:
                return True
            return False

