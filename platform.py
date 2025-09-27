import pygame
from collision_object import collision_object

class platform(collision_object):
    def __init__(self, position, size, image_path):
        collision_object.__init__(self, position, size)
        self.image = pygame.image.load(image_path)

    def draw(self, screen):
        screen.blit(self.image, self.position)