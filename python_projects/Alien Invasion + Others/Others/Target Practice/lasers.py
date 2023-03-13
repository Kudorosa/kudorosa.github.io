import pygame
from pygame.sprite import Sprite 

class Laser(Sprite): 
    """ """ 
    def __init__(self, game_settings, screen, ranger):
        """ """ 
        super().__init__() 
        self.screen = screen
        
        self.rect = pygame.Rect(0,0, game_settings.laser_width,
                                            game_settings.laser_height)
        self.rect.centerx = ranger.rect.centerx
        self.rect.center = ranger.rect.center
        
        self.x = float(self.rect.x)
        
        self.colour = game_settings.laser_colour
        self.speed = game_settings.laser_speed
        
    def update(self): 
        """ Allowing the Missle to Travel! """ 
        self.x -= self.speed
        self.rect.x = self.x
    
    def draw_laser(self): 
        """ Allow the Missle to be shown """ 
        pygame.draw.rect(self.screen, self.colour, self.rect) 
