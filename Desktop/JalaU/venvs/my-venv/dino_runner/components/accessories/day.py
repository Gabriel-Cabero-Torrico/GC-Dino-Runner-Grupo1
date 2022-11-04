import pygame
from pygame.sprite import Sprite
from utils.constants import DAY
from utils.constants import SCREEN_WIDTH
class Day(Sprite):
    def __init__(self):
        self.image = DAY[0]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = SCREEN_WIDTH
        self.image_rect.y = 10 
        self.day_Dino = True
        self.heigth = SCREEN_WIDTH     
            
    def update(self):
        self.image = DAY[0] if self.day_Dino == True else DAY[1] 
        self.image_rect = self.image.get_rect()
        if self.heigth > 0:
            self.image_rect.x = self.heigth                
            self.heigth -= 1        
            if self.heigth <= 0:
                self.heigth = SCREEN_WIDTH 
                self.day_Dino = not self.day_Dino
                          

    def draw(self, screen):
        screen.blit(self.image,(self.image_rect.x,self.image_rect.y))
         