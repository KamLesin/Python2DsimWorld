import math

from AlzurShield import AlzurShield
from Antelope import Antelope
from AntelopeSpeed import AntelopeSpeed
from Belladona import Belladona
from CyberSheep import CyberSheep
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
from Wolf import Wolf
from Human import Human
from Sheep import Sheep
from Fox import Fox
import random
import pygame


class HexWorld(World):
    def __init__(self, x, y):
        super().__init__(x, y)
        pygame.init()
        self.__gridWorld = False
        self.__done = False
        self.background = (0, 0, 0)
        self.free_tile = (255, 255, 255)
        self.window_size = [980, 640]
        self.buttons_place = [140, 209, 278]
        self.__margin = 1
        self.buttons_text = ["SAVE", "LOAD", "TURN"]
        self.screen = pygame.display.set_mode(self.window_size)
        self.font_text_and_buttons = pygame.font.SysFont('Arial', 18, True)
        self.font_board = pygame.font.SysFont('Arial', self.window_size[1] // self.min_number(self.x, self.y) // 3,
                                              True)
        self.__radius = (self.window_size[1] - int(self.x) * self.margin) // (int(self.x) * 13 / 4)
        self.dictionary = {"Human": Human, "Wolf": Wolf, "Sheep": Sheep, "Fox": Fox, "Turtle": Turtle,
                           "Antelope": Antelope,
                           "CyberSheep": CyberSheep, "Grass": Grass, "SowThistle": SowThistle, "Guarana": Guarana,
                           "Belladona": Belladona, "Hogweed": SosnowskyHogweed}

    @property
    def radius(self):
        return self.__radius

    @property
    def margin(self):
        return self.__margin

    @property
    def gridWorld(self):
        return self.__gridWorld

    def play(self):

        self.organisms.append(CyberSheep(0, 10, 0, 0, self))
        # self.organisms.append(Wolf(0, 0, 1, 0, self))
        # self.organisms.append(Turtle(0, 3, 3, self))
        # self.organisms.append(Sheep(5, 8, 8, self))
        # self.organisms.append(Sheep(12, 9, 9, self))
        # self.organisms.append(Antelope(0, 3, 3, self))
        # self.organisms.append(SosnowskyHogweed(0, 0, 7, 7, self))
        # self.organisms.append(SosnowskyHogweed(0, 0, 0, 0, self))
        self.organisms.sort(key=lambda o: (o.initiative, o.age), reverse=True)

        pygame.display.set_caption("Grid World")

        clock = pygame.time.Clock()

        while not self.__done:
            self.human = self.get_human()
            events = pygame.event.get()
            for event in events:
                self.event_handler(event)

            self.screen.fill(self.background)

            self.draw_screen(self.margin)

            clock.tick(60)

            pygame.display.flip()

        pygame.quit()

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if self.has_human() is True:
                    if self.human.position_y % 2 == 1:
                        self.human.speedY = -1
                    else:
                        self.human.speedY = -1
                        self.human.speedX = -1
                self.make_turn()
            elif event.key == pygame.K_w:
                if self.has_human() is True:
                    self.human.speedY = -2
                self.make_turn()
            elif event.key == pygame.K_e:
                if self.has_human() is True:
                    if self.human.position_y % 2 == 0:
                        self.human.speedY = -1
                    else:
                        self.human.speedY = -1
                        self.human.speedX = 1
                self.make_turn()
            elif event.key == pygame.K_a:
                if self.has_human() is True:
                    if self.human.position_y % 2 == 1:
                        self.human.speedY = 1
                    else:
                        self.human.speedY = 1
                        self.human.speedX = -1
                self.make_turn()
            elif event.key == pygame.K_s:
                if self.has_human() is True:
                    self.human.speedY = 2
                self.make_turn()
            elif event.key == pygame.K_d:
                if self.has_human() is True:
                    if self.human.position_y % 2 == 0:
                        self.human.speedY = 1
                    else:
                        self.human.speedY = 1
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
                        if j.position_x == mouse_pos[0] // self.radius and j.position_y == mouse_pos[1] // self.radius:
                            return
                        pos_x = mouse_pos[0] // self.radius // (13 / 4)
                        pos_y = mouse_pos[1] // self.radius // (7 / 6)
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
                        if self.has_human():
                            for n in self.human.abilities_cooldown:
                                out_file.write(str(self.human.abilities_cooldown[n]) + ' ')
                        out_file.write(str('\n'))
                        for j in self.organisms:
                            out_file.write(str(j.strength) + ' ')
                            out_file.write(str(j.age) + ' ')
                            out_file.write(str(j.position_x) + ' ')
                            out_file.write(str(j.position_y) + ' ')
                            out_file.write(j.name + '\n')
                        out_file.close()
                    elif self.buttons_text[i] == "LOAD":
                        self.action_text.append("_Loaded_")
                        self.organisms.clear()
                        file_name = input("input file name: ")
                        in_file = open(file_name, "r")
                        for line in in_file:
                            words = line.split()
                            self.organisms.append(
                                self.dictionary[words[4]](int(words[0]), int(words[1]), int(words[2]), int(words[3]),
                                                          self))
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
            rand = random.randint(1, 6)
            if rand == 1:
                if i.position_y % 2 == 1:
                    i.speedY = -1
                else:
                    i.speedY = -1
                    i.speedX = -1
            elif rand == 2:
                i.speedY = -2
            elif rand == 3:
                if i.position_y % 2 == 0:
                    i.speedY = -1
                else:
                    i.speedY = -1
                    i.speedX = 1
            elif rand == 4:
                if i.position_y % 2 == 1:
                    i.speedY = 1
                else:
                    i.speedY = 1
                    i.speedX = -1
            elif rand == 5:
                i.speedY = 2
            elif rand == 6:
                if i.position_y % 2 == 0:
                    i.speedY = 1
                else:
                    i.speedY = 1
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

    def draw_screen(self, margin):
        for row in range(int(self.y)):
            for column in range(int(self.x)):
                if self.has_organism(column, row, self.organisms):
                    color = self.find_organism(column, row, self.organisms).draw()[0]
                    pygame.draw.polygon(self.screen, color, self.create_vertices(column, row, margin))

                    self.text_to_surface_board(self.get_avg_vertices_x(column, row, margin) + self.radius * 2 / 3,
                                               self.get_avg_vertices_y(column, row, margin) - self.radius * 2 / 3,
                                               self.find_organism(column, row, self.organisms).draw()[1],
                                               self.background)

                else:
                    pygame.draw.polygon(self.screen, self.free_tile, self.create_vertices(column, row, margin))

        for i in range(len(self.buttons_place)):
            pygame.draw.rect(self.screen, self.free_tile, [self.window_size[1] + self.buttons_place[i], 10, 50, 30])
            self.text_to_surface(self.window_size[1] + self.buttons_place[i] + 7, 15, self.buttons_text[i],
                                 self.background)

        for i in range(len(self.action_text)):
            next_text = 23
            self.text_to_surface(self.window_size[1] + self.buttons_place[0], 14 * next_text + (i * next_text),
                                 self.action_text[i],
                                 self.free_tile)

    def get_avg_vertices_x(self, column, row, margin):
        sum_avg = 0
        for i in range(6):
            sum_avg += (margin * 3 + self.radius * 2) * column * 3 / 2 + (row % 2) * self.radius * 3 / 2
            + (row % 2) * margin * 2 + self.radius * math.cos(
                2 * math.pi * i / 6) + self.radius
        return sum_avg / 6

    def get_avg_vertices_y(self, column, row, margin):
        sum_avg = 0
        for i in range(6):
            sum_avg += (margin + self.radius) * row + self.radius * math.sin(
                2 * math.pi * i / 6) + self.radius
        return sum_avg / 6

    def create_vertices(self, column, row, margin):
        return [
            ((margin * 3 + self.radius * 2) * column * 3 / 2 + (row % 2) * self.radius * 3 / 2
             + (row % 2) * margin * 2 + self.radius * math.cos(
                2 * math.pi * i / 6) + self.radius,
             (margin + self.radius) * row + self.radius * math.sin(
                 2 * math.pi * i / 6) + self.radius)
            for i in range(6)
        ]
