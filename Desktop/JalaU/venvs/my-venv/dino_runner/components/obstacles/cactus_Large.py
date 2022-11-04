import random
from components.obstacles.obstacle import Obstacle

class Cactus_Large(Obstacle):
    def __init__(self, images):
        index = random.randint(0,3)
        super().__init__(images, index)
        self.image_rect.y = 300 