#TEST V-----------------------------------------------------------
import pygame 
from pygame.sprite import Group
from settings import Setting
import game_options as go
from helicopter import Helicopter

def start(): 
    """ Initiate the Game """ 
    pygame.init()
    settings = Setting()
    screen = pygame.display.set_mode((settings.screen_width, 
                                    settings.screen_height)) 
    pygame.display.set_caption("Rainfall") 
    colour = (settings.screen_colour)
    helicopter = Helicopter(screen, settings)
    turrets = Group()
    raindrops = Group()
    go.spawn_rain(settings, screen, helicopter, raindrops) 
    
    while True: 
        go.refresh_screen(settings, screen, helicopter, raindrops, turrets)
        go.event_check(settings, screen, helicopter, turrets) 
        helicopter.movement()
        go.update_rain(settings, screen, helicopter, raindrops)
        go.erasing_bullets(turrets)
    
start() 
    
