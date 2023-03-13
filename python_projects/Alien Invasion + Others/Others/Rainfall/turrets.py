import pygame
from pygame.sprite import Sprite

class Turret(Sprite): 
    """ """ 
    def __init__(self, settings, screen, helicopter):
        """ """ 
        super(Turret, self).__init__() 
        self.screen = screen
        
        self.rect = pygame.Rect(0,0, settings.bullets_width, 
                                                    settings.bullets_height)
        self.rect.centerx = helicopter.rect.centerx
        self.rect.bottom = helicopter.rect.bottom
        
        self.x = float(self.rect.x)
        
        self.colour = settings.bullets_colour
        self.speed = settings.bullets_speed
        
    def update(self): 
        """ Allowing the Missle to Travel! """ 
        self.x -= self.speed
        self.rect.x = self.x
    
    def draw_bullets(self): 
        """ Allow the Missle to be shown """ 
        pygame.draw.rect(self.screen, self.colour, self.rect) 
        
        
                                
