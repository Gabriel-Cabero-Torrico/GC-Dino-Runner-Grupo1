import pygame
from pygame.sprite import Sprite
from utils.constants import LIVE
from utils.constants import SCREEN_WIDTH
class Extra_Live(Sprite):
    def __init__(self):
        self.image = LIVE
        self.image_rect = self.image.get_rect()
        self.image_rect.x = SCREEN_WIDTH
        self.image_rect.y = 400 
        self.heigth = SCREEN_WIDTH 
        pygame.time.delay(1000)           
            
    def update(self):         
        self.image_rect = self.image.get_rect()
        if self.heigth > 0:
            self.image_rect.x = self.heigth                
            self.heigth -= 1        
            if self.heigth <= 0:
                self.heigth = SCREEN_WIDTH 
                pygame.time.delay(1000)                         

    def draw(self, screen):
        screen.blit(self.image,(self.image_rect.x,self.image_rect.y))