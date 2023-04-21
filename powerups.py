import pygame
import random
class Powerups:
    def __init__(self,win,player):
        self.player = player
        self.win = win
        self.is_PU_engage = True
        if self.player == "1":
            self.cords = (random.randint(0, 460), random.randint(5, 953))
        if self.player == "2":
            self.cords = (random.randint(540, 953), random.randint(5, 953))
    def make_PU(self):
            pygame.draw.rect(self.win, (0,0,255), (self.cords[0], self.cords[1], 10, 10))
    def if_PUtouch(self,player_cords):
        if self.cords[1] >= player_cords[1] and self.cords[1] <= player_cords[1] + 40 and \
                self.cords[0] >= player_cords[0] and self.cords[0] <= player_cords[0] + 40:
            return True
    def detete_PU(self):
        self.is_PU_engage = False
        if self.player == "1":
            self.cords = (random.randint(0, 460), random.randint(5, 953))
        if self.player == "2":
            self.cords = (random.randint(540,953), random.randint(5, 953))


