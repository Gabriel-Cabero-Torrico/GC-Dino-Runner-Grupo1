import random
import pygame
from utils.constants import BIRD

from components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        self.form = 0
        super().__init__(image, self.form)
        self.image_rect.y = 250 
        self.step = 1     
        self.helper = True  

    def update(self, speed): 
        self.image_rect.x -= speed
        if self.step <= 10:
            self.helper = True
        else:
            self.helper = False    
        self.step += 1
        if self.helper:
            self.form = 0 
        else:
            self.form = 1
        

    def draw(self, screen):
        screen.blit(self.image,(self.image_rect.x,self.image_rect.y))
        
         