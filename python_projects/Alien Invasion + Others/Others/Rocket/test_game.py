#TEST V-----------------------------------------------------------
import pygame 
from pygame.sprite import Group
from options import Option
import mechanics as m
from rocket import Rocket

def start(): 
    """ Initiate the Game """ 
    pygame.init()
    options = Option()
    screen = pygame.display.set_mode((options.screen_width, 
                                    options.screen_height)) 
    pygame.display.set_caption("Project 0") 
    colour = (options.screen_colour)
    rocket = Rocket(screen, options)
    missles = Group()
    stars = Group()
    m.summon_constellation(options, screen, rocket, stars) 
    
    while True: 
        m.refresh_screen(options, screen, rocket, stars, missles)
        m.event_check(options, screen, rocket, missles) 
        rocket.movement()
        m.erasing_missles(missles)
    
start() 
    
