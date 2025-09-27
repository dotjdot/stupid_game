#ya bois name is flint axlecrank

import pygame
from collision_object import collision_object

class flint(collision_object):
    _instance = None

    def __init__(self, position, screen, obstacle_list):
        if flint._instance is not None:
            raise Exception("Only one instance of flint allowed!")
        collision_object.__init__(self, position, (50, 50))
        self.screen = screen
        self.obstacle_list = obstacle_list
        self.image = pygame.image.load("sprites/flint.png")
        flint._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise Exception("No instance of flint exists yet!")
        return cls._instance

    def move(self, dx, dy):
        x, y = self.position
        new_position = (x + dx, y + dy)
        self.position = new_position
        self.rect.topleft = self.position  # Sync rect with position
        for obstacle in self.obstacle_list:
            if self.check_collision(obstacle.rect):
                direction = obstacle.get_overlap_direction(self.rect)
                if direction == 'left':
                    self.position = (obstacle.rect.right, y + dy)
                elif direction == 'right':
                    self.position = (obstacle.rect.left - self.size[0], y + dy)
                elif direction == 'up':
                    self.position = (x + dx, obstacle.rect.bottom)
                elif direction == 'down':
                    self.position = (x + dx, obstacle.rect.top - self.size[1])
                self.rect.topleft = self.position  # Sync rect after collision adjustment

    def draw(self):
        self.screen.blit(self.image, self.position)