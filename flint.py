#ya bois name is flint axlecrank

import pygame
from collision_object import collision_object
from collections import collections

TERMINAL_VELOCITY_X = 7
TERMINAL_VELOCITY_Y = 11
DRAG_X = 0.8
DRAG_Y = 0.2
JUMP_BOOST = 11
ACCELERATION_X = 0.9
JUMP_BUFFER_MAX = 6  # buffer window in frames
GROUND_TOLERANCE = 5  # pixels

class flint(collision_object):
    _instance = None

    def __init__(self, position, screen, obstacle_list):
        if flint._instance is not None:
            raise Exception("Only one instance of flint allowed!")
        collision_object.__init__(self, position, (75, 150))
        self.screen = screen
        self.obstacle_list = obstacle_list
        self.image = pygame.image.load("sprites/flint.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.v_x = 0
        self.v_y = 0
        self.on_ground = False
        self.jump_buffer = 0  # frames left to buffer a jump
        flint._instance = self
        self.collections = collections()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise Exception("No instance of flint exists yet!")
        return cls._instance
    
    def update_motion(self):
        self.on_ground = False  # Reset ground state each frame
        # Substep movement to prevent tunneling
        steps = int(max(abs(self.v_x), abs(self.v_y), 1))
        dx = self.v_x / steps
        dy = self.v_y / steps

        for _ in range(steps):
            self.position = (self.position[0] + dx, self.position[1] + dy)
            self.rect.topleft = (round(self.position[0]), round(self.position[1]))
            for obstacle in self.obstacle_list:
                if self.check_collision(obstacle.rect):
                    direction = obstacle.get_overlap_direction(self.rect)
                    if direction == 'left':
                        self.position = (obstacle.rect.right, self.position[1])
                        self.v_x = 0
                    elif direction == 'right':
                        self.position = (obstacle.rect.left - self.size[0], self.position[1])
                        self.v_x = 0
                    elif direction == 'up':
                        self.position = (self.position[0], obstacle.rect.bottom)
                        self.v_y = 0
                    elif direction == 'down':
                        y_diff = abs((self.position[1] + self.size[1]) - obstacle.rect.top)
                        if y_diff <= GROUND_TOLERANCE:
                            self.position = (self.position[0], obstacle.rect.top - self.size[1])
                            self.on_ground = True
                            self.v_y = 0
                    self.rect.topleft = (round(self.position[0]), round(self.position[1]))

        # Jump buffering: if a jump was requested recently and Flint is now on ground, jump immediately
        if self.on_ground and self.jump_buffer > 0:
            self.v_y = -JUMP_BOOST
            self.on_ground = False
            self.jump_buffer = 0
            print("jump executed from buffer")

        # apply drag forces
        if not self.on_ground:
            self.v_y = min(self.v_y + DRAG_Y, TERMINAL_VELOCITY_Y)  # gravity
        if self.v_x > 0:
            self.v_x -= DRAG_X  # drag right
            if self.v_x < 0:
                self.v_x = 0
        elif self.v_x < 0:
            self.v_x += DRAG_X  # drag left
            if self.v_x > 0:
                self.v_x = 0

        # Decrement jump buffer
        if self.jump_buffer > 0:
            self.jump_buffer -= 1

        #print(self.position, self.v_x, self.v_y, self.on_ground)
        return


    def run(self, direction):
        if direction == "left":
            self.v_x = max(self.v_x - ACCELERATION_X, -TERMINAL_VELOCITY_X)
        elif direction == "right":
            self.v_x = min(self.v_x + ACCELERATION_X, TERMINAL_VELOCITY_X)

        return
    
    def jump(self):
        # Set jump buffer so jump will occur as soon as Flint is on ground
        self.jump_buffer = JUMP_BUFFER_MAX
        return

    def draw(self):
        self.screen.blit(self.image, self.position)

        return