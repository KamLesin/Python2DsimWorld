import pygame

from Human import Human


class World:
    def __init__(self, x, y):
        self.__font_board = None
        self.__font_text_and_buttons = None
        self.__background = ()
        self.__screen = None
        self.__notDone = True
        self.__x = x
        self.__y = y
        self.__free_tile = ()
        self.__window_size = []
        self.__organisms = []
        self.__temp_organisms_add = []
        self.__temp_organisms_remove = []
        self.__buttons_place = []
        self.__buttons_text = []
        self.__human = None
        self.__dictionary = {}
        self.__action_text = []
        self.__all_organism_types = ["Human", "Wolf", "Sheep", "Fox", "Turtle", "Antelope", "CyberSheep", "Grass",
                                   "SowThistle", "Guarana", "Belladona", "Hogweed"]
        self.__all_abilities_names = ["Immortality", "MPotion", "ASpeed", "AShield", "Purification"]

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, new_bg):
        self.__background = new_bg

    @property
    def action_text(self):
        return self.__action_text

    @action_text.setter
    def action_text(self, new_text):
        self.__action_text = new_text

    @property
    def font_board(self):
        return self.__font_board

    @font_board.setter
    def font_board(self, new_f_board):
        self.__font_board = new_f_board

    @property
    def font_text_and_buttons(self):
        return self.__font_text_and_buttons

    @font_text_and_buttons.setter
    def font_text_and_buttons(self, new_f):
        self.__font_text_and_buttons = new_f

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, new_screen):
        self.__screen = new_screen

    @property
    def notDone(self):
        return self.__notDone

    @notDone.setter
    def notDone(self, new_notDone):
        self.__notDone = new_notDone

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def free_tile(self):
        return self.__free_tile

    @free_tile.setter
    def free_tile(self, new_tile):
        self.__free_tile = new_tile

    @property
    def window_size(self):
        return self.__window_size

    @window_size.setter
    def window_size(self, new_size):
        self.__window_size = new_size

    @property
    def organisms(self):
        return self.__organisms

    @property
    def temp_organisms_add(self):
        return self.__temp_organisms_add

    @property
    def temp_organisms_remove(self):
        return self.__temp_organisms_remove

    @property
    def buttons_place(self):
        return self.__buttons_place

    @buttons_place.setter
    def buttons_place(self, new_places):
        self.__buttons_place = new_places

    @property
    def buttons_text(self):
        return self.__buttons_text

    @buttons_text.setter
    def buttons_text(self, new_text):
        self.__buttons_text = new_text

    @property
    def human(self):
        return self.__human

    @human.setter
    def human(self, new_h):
        self.__human = new_h

    @property
    def dictionary(self):
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, new_dict):
        self.__dictionary = new_dict

    @property
    def all_organism_types(self):
        return self.__all_organism_types

    @property
    def all_abilities_names(self):
        return self.__all_abilities_names

    def get_human(self):
        for i in self.organisms:
            if isinstance(i, Human):
                return i

    def is_not_on_list(self, organism):
        for i in self.organisms:
            if i.position_y == organism.position_y and i.position_x == organism.position_x:
                return False
        return True

    def text_to_surface(self, x, y, text, color):
        self.screen.blit(self.__font_text_and_buttons.render(text, False, color), (x, y))

    def text_to_surface_board(self, x, y, text, color):
        self.screen.blit(self.font_board.render(text, False, color), (x, y))

    def has_organism(self, x, y, organisms):
        for i in range(len(organisms)):
            if x == organisms[i].position_x and y == organisms[i].position_y:
                return True

    def find_organism(self, x, y, organisms):
        for i in range(len(organisms)):
            if x == organisms[i].position_x and y == organisms[i].position_y:
                return organisms[i]

    def has_human(self):
        for i in self.organisms:
            if isinstance(i, Human):
                return True
        return False

    def add_organism_next_turn(self, strength, age, pos_x, pos_y, name):
        self.temp_organisms_add.append(self.dictionary[name](strength, age, pos_x, pos_y, self))

    def remove_organism_next_turn(self, organism):
        organism.died = True
        self.temp_organisms_remove.append(organism)

    def min_number(self, x, y):
        if x < y:
            return x
        return y

    def max_number(self, x, y):
        if x > y:
            return x
        return y

    def create_choice(self):
        for i in range(len(self.all_organism_types)):
            self.text_to_surface(self.window_size[1] + 20, 23 * i, self.all_organism_types[i], self.free_tile)
        while self.notDone:

            pygame.display.flip()
            string_o = self.get_input()
        self.notDone = True
        return string_o

    def get_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(len(self.all_organism_types)):
                    if 23 * i < mouse_pos[1] < 23 * i + 23 and self.window_size[0] - 200 > mouse_pos[0] > self.window_size[1]:
                        self.notDone = False
                        return self.all_organism_types[i]
