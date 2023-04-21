

class SpecialAbility:
    def __init__(self):
        self.__duration_left = 5

    @property
    def duration_left(self):
        return self.__duration_left

    @duration_left.setter
    def duration_left(self, new_d):
        self.__duration_left = new_d

    def giveName(self):
        pass
