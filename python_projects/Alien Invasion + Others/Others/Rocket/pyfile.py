#TEST V----------------------------
import pygame
import sys
from options import Option

def engage(): 
    """ Detecting Input """ 
    pygame.init()
    options = Option() 
    screen = pygame.display.set_mode((options.screen_width, 
                                        options.screen_height))
    pygame.display.set_caption("Detector 9000") 
    
    while True:
        pygame.display.flip()
        screen.fill(options.screen_colour) 
        for event in pygame.event.get(): 
            if event == "QUIT":
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("UP") 
                    options.screen_colour = (250,0,0) 
                if event.key == pygame.K_DOWN: 
                    print("DOWN") 
                    options.screen_colour = (0,250,0) 
                if event.key == pygame.K_LEFT: 
                    print("LEFT") 
                    options.screen_colour = (0,0,250) 
                if event.key == pygame.K_RIGHT:
                    print("RIGHT") 
                    options.screen_colour = (250,250,0) 

engage() 
