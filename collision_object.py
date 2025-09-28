import pygame


class collision_object:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position, size)

    def check_collision(self, other_rect):
        result = self.rect.colliderect(other_rect)
        #print(f"[DEBUG] check_collision: self={self.rect}, other={other_rect}, result={result}")
        return result
    
    def get_overlap_direction(self, other_rect):
        if not self.check_collision(other_rect):
            #print("[DEBUG] get_overlap_direction: No collision detected.")
            return None

        # Calculate overlap in each direction
        dx_left = self.rect.right - other_rect.left
        dx_right = other_rect.right - self.rect.left
        dy_top = self.rect.bottom - other_rect.top
        dy_bottom = other_rect.bottom - self.rect.top

        # Find the smallest positive overlap
        overlaps = {
            'left': dx_left,
            'right': dx_right,
            'up': dy_top,
            'down': dy_bottom
        }
        # Only consider positive overlaps (actual intersection)
        positive_overlaps = {k: v for k, v in overlaps.items() if v >= 0}
        if not positive_overlaps:
            #print("[DEBUG] get_overlap_direction: No positive overlaps.")
            return None
        min_dir = min(positive_overlaps, key=positive_overlaps.get)
        #print(f"[DEBUG] get_overlap_direction: overlaps={overlaps}, min_dir={min_dir}")
        return min_dir