class Organism:
    def __init__(self, strength, initiative, age, position_x, position_y, world, name):
        self.__strength = strength
        self.__initiative = initiative
        self.__age = age
        self.__position_x = position_x
        self.__position_y = position_y
        self.__world = world
        self.__name = name
        self.__died = False

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, new_s):
        self.__strength = new_s

    @property
    def initiative(self):
        return self.__initiative

    @initiative.setter
    def initiative(self, new_i):
        self.__initiative = new_i

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_a):
        self.__age = new_a

    @property
    def position_x(self):
        return self.__position_x

    @position_x.setter
    def position_x(self, new_x):
        self.__position_x = new_x

    @property
    def position_y(self):
        return self.__position_y

    @position_y.setter
    def position_y(self, new_y):
        self.__position_y = new_y

    @property
    def world(self):
        return self.__world

    @world.setter
    def world(self, new_w):
        self.__world = new_w

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_n):
        self.__name = new_n

    @property
    def died(self):
        return self.__died

    @died.setter
    def died(self, new_d):
        self.__died = new_d

    def draw(self):
        pass

    def action(self, organisms):
        pass

    def collision(self, organism):
        pass

    def free_pos_xy(self):
        if self.world.gridWorld is True:
            if self.position_y - 1 >= 0 and self.check_free_pos(self.position_x, self.position_y - 1) is True:
                return [self.position_x, self.position_y - 1]
            elif self.position_x - 1 >= 0 and self.check_free_pos(self.position_x - 1, self.position_y) is True:
                return [self.position_x - 1, self.position_y]
            elif self.position_x + 1 < self.world.x and self.check_free_pos(self.position_x + 1, self.position_y) is True:
                return [self.position_x + 1, self.position_y]
            elif self.position_y + 1 < self.world.y and self.check_free_pos(self.position_x, self.position_y + 1) is True:
                return [self.position_x, self.position_y + 1]
            else:
                return [self.position_x, self.position_y]
        else:
            if self.position_y % 2 == 1:
                if self.position_y - 1 >= 0 and self.check_free_pos(self.position_x, self.position_y - 1) is True:
                    return[self.position_x, self.position_y - 1]
                elif self.position_y - 2 >= 0 and self.check_free_pos(self.position_x, self.position_y - 2) is True:
                    return [self.position_x, self.position_y - 2]
                elif self.position_y - 1 >= 0 and self.position_x + 1 < self.world.x and self.check_free_pos(self.position_x + 1, self.position_y - 1) is True:
                    return [self.position_x + 1, self.position_y - 1]
                elif self.position_y + 1 < self.world.y and self.position_x + 1 < self.world.x and self.check_free_pos(self.position_x + 1, self.position_y + 1) is True:
                    return [self.position_x + 1, self.position_y + 1]
                elif self.position_y + 2 < self.world.y and self.check_free_pos(self.position_x, self.position_y + 2) is True:
                    return [self.position_x, self.position_y + 2]
                elif self.position_y + 1 < self.world.y and self.check_free_pos(self.position_x, self.position_y + 1) is True:
                    return [self.position_x, self.position_y + 1]
                else:
                    return [self.position_x, self.position_y]
            else:
                if self.position_y - 1 >= 0 and self.check_free_pos(self.position_x, self.position_y - 1) is True:
                    return[self.position_x, self.position_y - 1]
                elif self.position_y - 2 >= 0 and self.check_free_pos(self.position_x, self.position_y - 2) is True:
                    return [self.position_x, self.position_y - 2]
                elif self.position_y - 1 >= 0 and self.position_x - 1 > 0 and self.check_free_pos(self.position_x - 1, self.position_y - 1) is True:
                    return [self.position_x - 1, self.position_y - 1]
                elif self.position_y + 1 < self.world.y and self.position_x - 1 >= 0 and self.check_free_pos(self.position_x - 1, self.position_y + 1) is True:
                    return [self.position_x - 1, self.position_y + 1]
                elif self.position_y + 2 < self.world.y and self.check_free_pos(self.position_x, self.position_y + 2) is True:
                    return [self.position_x, self.position_y + 2]
                elif self.position_y + 1 < self.world.y and self.check_free_pos(self.position_x, self.position_y + 1) is True:
                    return [self.position_x, self.position_y + 1]
                else:
                    return [self.position_x, self.position_y]

    def check_free_pos(self, x, y):
        for i in self.world.organisms:
            if i.position_x == x and i.position_y == y:
                return False
        return True
