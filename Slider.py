import pygame
class slider:
    def __init__(self,win,slider_cords,min,max,sl_movement_speed):
        self.sl_cords = slider_cords
        self.max = max
        self.min = min
        self.win = win
        self.sl_wid = 300
        self.sl_len = 10
        self.bar_wid = 10
        self.bar_len = 40
        self.sl_speed = sl_movement_speed
        self.bar_cords = [self.sl_cords[0]+150,self.sl_cords[1]-15]
        self.bar_pos = self.min + ((self.max-self.min)/2)
    def draw(self):
        sl_x,sl_y = self.sl_cords
        bar_x,bar_y = self.bar_cords
        RED = (255,0,0)
        GRAY = (188,188,188)
        #main slider
        pygame.draw.rect(self.win, RED, (sl_x, sl_y, self.sl_wid, self.sl_len))
        #bar that moves
        pygame.draw.rect(self.win,GRAY,(bar_x,bar_y,self.bar_wid,self.bar_len))
    def move_slider(self, x,y):
        if y >= self.sl_cords[1] - 20 and y <= self.sl_cords[1] + 40:
            if x >= self.sl_cords[0] and x < self.sl_cords[0] + 301:
                if x > self.bar_cords[0]:
                    self.bar_pos = round((self.bar_pos + self.sl_speed),7)
                if x < self.bar_cords[0]:
                    self.bar_pos = round((self.bar_pos - self.sl_speed),7)
                self.bar_cords[0] = x



