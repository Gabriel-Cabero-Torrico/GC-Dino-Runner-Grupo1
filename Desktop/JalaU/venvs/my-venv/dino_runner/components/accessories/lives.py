import pygame
from pygame.sprite import Sprite
from utils.constants import DINO_LIVES

class Lives(Sprite):
    def __init__(self):
        self.image = DINO_LIVES[0]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 100
        self.image_rect.y = 70 
        self.pos = 0  
            
    def update(self):
        self.image = DINO_LIVES[self.pos]          

    def draw(self, screen):
        screen.blit(self.image,(self.image_rect.x,self.image_rect.y))