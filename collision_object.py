import pygame


class collision_object:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position, size)

    def check_collision(self, other_rect):
        return self.rect.colliderect(other_rect)
    
    def get_overlap_direction(self, other_rect):
        if not self.check_collision(other_rect):
            return None

        dx = (self.rect.centerx - other_rect.centerx)
        dy = (self.rect.centery - other_rect.centery)

        if abs(dx) > abs(dy):
            return 'left' if dx < 0 else 'right'
        else:
            return 'up' if dy < 0 else 'down'