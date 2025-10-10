import pygame

class collectible_object:
    def __init__(self, position, size, image_path, type):
        self.position = position
        self.size = size
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = pygame.Rect(position, size)
        self.type = type 


    def draw(self, screen):
        screen.blit(self.image, self.position)
