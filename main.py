import pygame
import sys
from flint import flint
from platform_object import platform_object

def handle_kepress_hold():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        flint.get_instance().run("left")
    if keys[pygame.K_d]:
        flint.get_instance().run("right")

def handle_keypress_events(event):
    match event.key:
        case pygame.K_SPACE:
            flint.get_instance().jump()
            print("jump")

        case pygame.K_w:
            flint.get_instance().jump()


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
    pygame.init()

    # Set up the window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("My First Pygame Window")

    #create the obstacles
    obstacle_list = []
    obstacle_list.append(platform_object((0, 580), (800, 20), "sprites/mushroom.png"))
    obstacle_list.append(platform_object((0, 0), (20, 600), "sprites/mushroom.png"))
    obstacle_list.append(platform_object((0, 0), (800, 20), "sprites/mushroom.png"))
    obstacle_list.append(platform_object((780, 0), (20, 600), "sprites/mushroom.png"))
    obstacle_list.append(platform_object((600, 400), (100, 100), "sprites/mushroom.png"))
    obstacle_list.append(platform_object((300, 200), (100, 100), "sprites/mushroom.png"))

    #make flint
    flint((100,400), screen, obstacle_list)

    # Main loop
    running = True
    clock = pygame.time.Clock()
    while running:

        # Event handling
        for event in pygame.event.get():
            running = handle_events(event)

        #keypress holding 
        handle_kepress_hold()

        # update moving thingies
        flint.get_instance().update_motion()

        # rendering
        screen.fill((30, 30, 30))
        for obstacle in obstacle_list:
            obstacle.draw(screen)
        flint.get_instance().draw()
        pygame.display.flip()
        clock.tick(250)  # Limit the FPS/TPS

    pygame.quit()
    sys.exit()
    
    
    return

if __name__ == "__main__":
    main()