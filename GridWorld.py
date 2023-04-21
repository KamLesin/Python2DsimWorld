from AlzurShield import AlzurShield
from Antelope import Antelope
from AntelopeSpeed import AntelopeSpeed
from Belladona import Belladona
from CyberSheep import CyberSheep
from Fox import Fox
from Grass import Grass
from Guarana import Guarana
from Immortality import Immortality
from MagicalPotion import MagicalPotion
from Plant import Plant
from Purification import Purification
from SosnowskyHogweed import SosnowskyHogweed
from SowThistle import SowThistle
from Turtle import Turtle
from World import World
import random
import pygame
from Wolf import Wolf
from Human import Human
from Sheep import Sheep


class GridWorld(World):
    def __init__(self, x, y):
        super().__init__(x, y)

        pygame.init()
        self.__gridWorld = True
        self.__done = False
        self.background = (0, 0, 0)
        self.free_tile = (255, 255, 255)
        self.window_size = [980, 640]
        self.buttons_place = [104, 181, 258]
        self.__margin = 1
        self.__height = (self.window_size[1] - int(self.y) * self.__margin) // int(self.y)
        self.__width = (self.window_size[1] - int(self.x) * self.__margin) // int(self.x)
        self.buttons_text = ["SAVE", "LOAD", "TURN"]
        self.screen = pygame.display.set_mode(self.window_size)
        self.font_text_and_buttons = pygame.font.SysFont('Arial', 18, True)
        self.font_board = pygame.font.SysFont('Arial', self.window_size[1] // self.max_number(self.x, self.y), True)
        self.dictionary = {"Human": Human, "Wolf": Wolf, "Sheep": Sheep, "Fox": Fox, "Turtle": Turtle,
                           "Antelope": Antelope,
                           "CyberSheep": CyberSheep, "Grass": Grass, "SowThistle": SowThistle, "Guarana": Guarana,
                           "Belladona": Belladona, "Hogweed": SosnowskyHogweed}

    @property
    def margin(self):
        return self.__margin

    @property
    def gridWorld(self):
        return self.__gridWorld

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def play(self):

        self.organisms.append(Human(0, 0, 0, 1, self))
        self.organisms.append(CyberSheep(0, 5, 0, 0, self))

        pygame.display.set_caption("Grid World")

        clock = pygame.time.Clock()

        while not self.__done:
            self.human = self.get_human()
            events = pygame.event.get()
            for event in events:
                self.event_handler(event)

            self.screen.fill(self.background)

            self.draw_screen(self.width, self.height, self.__margin)

            clock.tick(60)

            pygame.display.flip()

        pygame.quit()

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.has_human() is True:
                    self.human.speedY = -1
                self.make_turn()
            elif event.key == pygame.K_DOWN:
                if self.has_human() is True:
                    self.human.speedY = 1
                self.make_turn()
            elif event.key == pygame.K_LEFT:
                if self.has_human() is True:
                    self.human.speedX = -1
                self.make_turn()
            elif event.key == pygame.K_RIGHT:
                if self.has_human() is True:
                    self.human.speedX = 1
                self.make_turn()
            elif event.key == pygame.K_ESCAPE:
                self.__done = True
            elif event.key == pygame.K_i:
                if self.has_human() is True:
                    if self.human.specialAbility is None and self.human.abilities_cooldown["Immortality"] == 0:
                        self.action_text.append("Immortality started!")
                        self.human.specialAbility = Immortality()
                    else:
                        self.action_text.append("You cant use it now!")
            elif event.key == pygame.K_m:
                if self.has_human() is True:
                    if self.human.specialAbility is None and self.human.abilities_cooldown["MPotion"] == 0:
                        self.action_text.append("MPotion started!")
                        self.human.specialAbility = MagicalPotion()
                        self.human.strength += 5
                    else:
                        self.action_text.append("You cant use it now!")
            elif event.key == pygame.K_l:
                if self.has_human() is True:
                    if self.human.specialAbility is None and self.human.abilities_cooldown["ASpeed"] == 0:
                        self.action_text.append("ASpeed started!")
                        self.human.specialAbility = AntelopeSpeed()
                    else:
                        self.action_text.append("You cant use it now!")
            elif event.key == pygame.K_n:
                if self.has_human() is True:
                    if self.human.specialAbility is None and self.human.abilities_cooldown["AShield"] == 0:
                        self.action_text.append("AShield started!")
                        self.human.specialAbility = AlzurShield()
                    else:
                        self.action_text.append("You cant use it now!")
            elif event.key == pygame.K_p:
                if self.has_human() is True:
                    if self.human.specialAbility is None and self.human.abilities_cooldown["Purification"] == 0:
                        self.action_text.append("Purification started!")
                        self.human.specialAbility = Purification()
                    else:
                        self.action_text.append("You cant use it now!")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(len(self.buttons_place)):
                if mouse_pos[0] < self.window_size[1] and mouse_pos[1] < self.window_size[1]:
                    for j in self.organisms:
                        if j.position_x == mouse_pos[0] // self.x and j.position_y == mouse_pos[1] // self.y:
                            return
                        pos_x = mouse_pos[0] // self.width
                        pos_y = mouse_pos[1] // self.height
                        name = self.create_choice()
                        self.add_organism_next_turn(0, 0, int(pos_x), int(pos_y), name)
                        self.add_and_remove_organisms()
                        break
                    break
                elif self.buttons_place[i] + self.window_size[1] <= mouse_pos[0] <= self.window_size[1] + \
                        self.buttons_place[i] + 50 and 10 <= mouse_pos[1] <= 30:
                    if self.buttons_text[i] == "SAVE":
                        self.action_text.append("_Saved_")
                        file_name = input("input file name: ")
                        out_file = open(file_name, "a")
                        for j in self.organisms:
                            out_file.write(str(j.strength) + ' ')
                            out_file.write(str(j.age) + ' ')
                            out_file.write(str(j.position_x) + ' ')
                            out_file.write(str(j.position_y) + ' ')
                            out_file.write(j.name + '\n')
                        if self.has_human():
                            out_file.write("Dictionary ")
                            out_file.write(self.human.specialAbility.giveName() + ' ' + str(self.human.specialAbility.duration_left) + ' ')
                            for n in self.human.abilities_cooldown:
                                out_file.write(str(self.human.abilities_cooldown[n]) + ' ')
                        out_file.write(str('\n'))
                        out_file.close()
                    elif self.buttons_text[i] == "LOAD":
                        self.action_text.append("_Loaded_")
                        self.organisms.clear()
                        file_name = input("input file name: ")
                        in_file = open(file_name, "r")
                        for line in in_file:
                            words = line.split()
                            if words[0] == "Dictionary":
                                self.human = self.get_human()
                                self.human.specialAbility = self.human.abilities_names[words[1]]()
                                self.human.specialAbility.duration_left = int(words[2])
                                for c in range(5):
                                    self.human.abilities_cooldown[self.all_abilities_names[c]] = int(words[c + 3])
                                break
                            self.organisms.append(self.dictionary[words[4]](int(words[0]), int(words[1]), int(words[2]), int(words[3]), self))
                    elif self.buttons_text[i] == "TURN":
                        self.make_turn()
        elif event.type == pygame.QUIT:
            self.__done = True

    def make_turn(self):
        self.action_text.clear()
        for i in self.organisms:
            if i.died is True:
                continue
            if isinstance(i, Human):
                i.action(self.organisms)
                continue
            rand = random.randint(1, 4)
            if rand == 1:
                i.speedY = -1
            elif rand == 2:
                i.speedY = 1
            elif rand == 3:
                i.speedX = -1
            elif rand == 4:
                i.speedX = 1
            i.action(self.organisms)
        self.add_and_remove_organisms()
        self.organisms.sort(key=lambda o: (o.initiative, o.age), reverse=True)

    def add_and_remove_organisms(self):
        for i in self.temp_organisms_remove:
            if self.is_not_on_list(i) is False:
                self.organisms.remove(i)
                self.action_text.append(i.name + " has died!")
        self.temp_organisms_remove.clear()
        for i in self.temp_organisms_add:
            if self.is_not_on_list(i) is True:
                self.organisms.append(i)
                if isinstance(i, Plant):
                    self.action_text.append(i.name + " has sowed!")
                else:
                    self.action_text.append(i.name + " has born!")
        self.temp_organisms_add.clear()

    def draw_screen(self, width, height, margin):
        for row in range(int(self.y)):
            for column in range(int(self.x)):
                if self.has_organism(column, row, self.organisms):
                    color = self.find_organism(column, row, self.organisms).draw()[0]
                    pygame.draw.rect(self.screen, color,
                                     [(margin + width) * column + margin, (margin + height) * row + margin, width,
                                      height])
                    self.text_to_surface_board((margin + width) * column + (width // 2) - (
                                (self.window_size[1] // self.max_number(self.x, self.y)) // 4),
                                               (margin + height) * row + (height // 2) -
                                               ((self.window_size[1] // self.max_number(self.x, self.y)) // 2),
                                               self.find_organism(column, row, self.organisms).draw()[1],
                                               self.background)
                else:
                    pygame.draw.rect(self.screen, self.free_tile,
                                     [(margin + width) * column + margin, (margin + height) * row + margin, width,
                                      height])
        for i in range(len(self.buttons_place)):
            pygame.draw.rect(self.screen, self.free_tile, [self.window_size[1] + self.buttons_place[i], 10, 50, 30])
            self.text_to_surface(self.window_size[1] + self.buttons_place[i] + 7, 15, self.buttons_text[i],
                                 self.background)
        for i in range(len(self.action_text)):
            next_text = 23
            self.text_to_surface(self.window_size[1] + self.buttons_place[0], 14 * next_text + (i * next_text),
                                 self.action_text[i],
                                 self.free_tile)
