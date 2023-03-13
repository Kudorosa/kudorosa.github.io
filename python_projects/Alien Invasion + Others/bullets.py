import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite): 
    """ Creating Bullets for the Ship to Fire! """  

    def __init__(self, game_settings, screen, ship): 
        """ """ 
        super(Bullet, self).__init__()#Python 2.7 Syntax
        self.screen = screen
        
        #Creating Bullet Rect at 0.0
        self.rect = pygame.Rect(0,0, game_settings.bullet_width,
                                            game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        self.y = float(self.rect.y)
        
        self.colour = game_settings.bullet_colour
        self.bullet_speed = game_settings.bullet_speed
        
    def update(self): 
        """ Allowing the Bullet to Travel """ 
        self.y -= self.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self): 
        """ Drawing the Bullet """ 
        pygame.draw.rect(self.screen, self.colour, self.rect)
