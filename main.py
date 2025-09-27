import pygame
import sys
from flint import flint
from platform import platform



def handle_keypress_events(event):
    match event.key:
        case pygame.K_w:
            flint.get_instance().move(0, -20)
        case pygame.K_a:
            flint.get_instance().move(-20, 0)
        case pygame.K_s:
            flint.get_instance().move(0, 20)
        case pygame.K_d:
            flint.get_instance().move(20, 0)


    return

def handle_events(event):
    match event.type:
        case pygame.QUIT:
            return False
        case pygame.KEYDOWN:
            handle_keypress_events(event)
        case pygame.MOUSEBUTTONDOWN:
            print("Mouse clicked at", event.pos)

    return True

def main():

    # Initialize Pygame

    # Set up the window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("My First Pygame Window")

    #create the obstacles
    obstacle_list = []
    obstacle_list.append(platform((400, 450), (100, 100), "sprites/mushroom.png"))

    #make flint
    flint((0,0), screen, obstacle_list)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            running = handle_events(event)

        # Fill the screen with a color (RGB)
        screen.fill((30, 30, 30))
        for obstacle in obstacle_list:
            obstacle.draw(screen)
        flint.get_instance().draw()
        pygame.display.flip()

    pygame.quit()
    sys.exit()
    
    
    return

if __name__ == "__main__":
    main()