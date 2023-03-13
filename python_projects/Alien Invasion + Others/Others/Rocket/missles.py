import pygame
from pygame.sprite import Sprite

class Missle(Sprite): 
    """ """ 
    def __init__(self, options, screen, rocket):
        """ """ 
        super().__init__() 
        self.screen = screen
        
        self.rect = pygame.Rect(0,0, options.missle_width, 
                                                        options.missle_height)
        self.rect.centerx = rocket.rect.centerx
        self.rect.bottom = rocket.rect.bottom
        
        self.x = float(self.rect.x)
        
        self.colour = options.missle_colour
        self.speed = options.missle_speed
        
    def update(self): 
        """ Allowing the Missle to Travel! """ 
        self.x -= self.speed
        self.rect.x = self.x
    
    def draw_missle(self): 
        """ Allow the Missle to be shown """ 
        pygame.draw.rect(self.screen, self.colour, self.rect) 
        
        
                                
