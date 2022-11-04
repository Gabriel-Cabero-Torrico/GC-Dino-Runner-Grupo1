import pygame
from pygame.sprite import Sprite
from utils.constants import RUNNING
from utils.constants import JUMPING
from utils.constants import DUCKING
from utils.constants import DINO_DEFENDER
from utils.constants import DINO_HAMMER
class Dinosaur(Sprite):
    DINO_X_POS = 50
    DINO_Y_POS = 300
    INTIAL_SEP =0
    MAX_STEP = 10
    def __init__(self):
        self.image = RUNNING[2]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS
        self.step = 0
        self.dino_jump = False
        self.dino_run = True
        self.dino_bend = False
        self.dino_guard = False
        self.dino_hammer = False
        self.helper = True
        self.points_life = 3

    def update(self, dino_event):
        if self.dino_jump:
            self.jump()
        if self.dino_run:
            self.run()
        if self.dino_bend:
            self.bend()
        if self.dino_guard:
            self.guard()
        if self.dino_hammer:
            self.hammer()

        if dino_event[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_bend = False
            self.dino_jump = True
            self.dino_guard = False
            self.dino_hammer = False

        elif dino_event[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_bend = True
            self.dino_jump = False
            self.dino_guard = False
            self.dino_hammer = False

        elif dino_event[pygame.K_RIGHT] and not self.dino_jump:
            self.dino_run = False
            self.dino_bend = False
            self.dino_jump = False
            self.dino_guard = True
            self.dino_hammer = False

        elif dino_event[pygame.K_LEFT] and not self.dino_jump:
            self.dino_run = False
            self.dino_bend = False
            self.dino_jump = False
            self.dino_guard = False
            self.dino_hammer = True

        elif not self.dino_jump:
            self.dino_run = True
            self.dino_bend = False
            self.dino_jump = False
            self.dino_guard = False
            self.dino_hammer = False

        if self.step > self.MAX_STEP:
            self.step = self.INTIAL_SEP

    def run(self):
        self.image = RUNNING[0] if self.step <= 5 else RUNNING[1] 
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS
        self.step += 1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            if self.image_rect.y > 110 and self.helper:
                self.image_rect.y -= 20                
            else:
                self.helper = False
                if self.image_rect.y < self.DINO_Y_POS:
                    self.image_rect.y += 20
                else:
                    self.dino_jump = False
                    self.dino_run = True
                    self.dino_bend = False
                    self.dino_guard = False
                    self.dino_hammer = False
                    self.helper = True

    def bend(self):
        self.image = DUCKING[0] if self.step <= 5 else DUCKING[1] 
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS + 40
        self.step += 1

    def guard(self):
        self.image = DINO_DEFENDER[0] if self.step <= 5 else DINO_DEFENDER[1] 
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS
        self.step += 1

    def hammer(self):
        self.image = DINO_HAMMER[0] if self.step <= 5 else DINO_HAMMER[1] 
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS
        self.step += 1

    def draw(self, screen):
        screen.blit(self.image,(self.image_rect.x,self.image_rect.y))
    def points_Lives(self):
        return self.points_life
