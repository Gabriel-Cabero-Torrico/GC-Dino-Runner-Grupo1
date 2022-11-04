import pygame
from pygame.sprite import Sprite
from utils.constants import CLOUD
from utils.constants import SCREEN_WIDTH
class Sky(Sprite):
    def __init__(self):
        self.image = CLOUD
        self.image_rect = self.image.get_rect()
        self.image_rect.x = SCREEN_WIDTH
        self.image_rect.y = 100 
        self.heigth = SCREEN_WIDTH              

    def update(self):
        self.image = CLOUD 
        self.image_rect = self.image.get_rect()
        if self.heigth > 0:
            self.image_rect.x = self.heigth
        self.image_rect.y = 100
        self.heigth -= 10        
        if self.heigth <= 0:
            self.heigth = SCREEN_WIDTH        
        
    def draw(self, screen):
        screen.blit(self.image,(self.image_rect.x,self.image_rect.y))