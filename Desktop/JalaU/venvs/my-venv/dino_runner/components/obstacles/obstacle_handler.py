import pygame
import random
from utils.constants import SMALL_CACTUS
from utils.constants import LARGE_CACTUS
from utils.constants import BIRD
from components.obstacles.cactus import Cactus
from components.obstacles.cactus_Large import Cactus_Large
from components.obstacles.bird import Bird
class ObstacleHandler(Cactus):    
    def __init__(self):
        self.obstacles = []        
        
    def update(self, speed, dino, lives):
        obstacles_dino = [Cactus(SMALL_CACTUS),Cactus_Large(LARGE_CACTUS),Bird(BIRD)]
        if len(self.obstacles) == 0:
            self.obstacles.append(obstacles_dino[random.randint(0,2)])           
        for obstacle in self.obstacles:
            obstacle.update(speed)
            if dino.image_rect.colliderect(obstacle.image_rect):
                pygame.time.delay(200)                
                self.obstacles.pop()  
                if not ((obstacle.image == LARGE_CACTUS[3] and dino.dino_guard) or (obstacle.image == SMALL_CACTUS[3] and dino.dino_hammer)):
                    dino.points_life -= 1
                    lives.pos += 1

            if obstacle.image_rect.x < obstacle.image_rect.width:
                self.obstacles.pop()

    def draw(self , screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)