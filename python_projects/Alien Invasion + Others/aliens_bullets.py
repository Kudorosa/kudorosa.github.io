import pygame
from pygame.sprite import Sprite 

class AlienBullet(Sprite): 
    """ Creating AlienBullets for the Ship to Fire! """  

    def __init__(self, game_settings, screen, aliens): 
        """ """ 
        super(AlienBullet, self).__init__()#Python 2.7 Syntax
        self.screen = screen
        
        #Creating AlienBullet Rect at 0.0
        self.rect = pygame.Rect(0,0, game_settings.bullet_width,
                                            game_settings.bullet_height)
        for alien in aliens.sprites():
            self.rect.centerx = alien.rect.centerx
            self.rect.bottom = alien.rect.bottom
        
        self.y = float(self.rect.y)
        
        self.colour = game_settings.alien_bullet_colour
        self.bullet_speed = game_settings.alien_bullet_speed
        
    def update(self): 
        """ Allowing the AlienBullet to Travel """ 
        self.y += self.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self): 
        """ Drawing the AlienBullet """ 
        pygame.draw.rect(self.screen, self.colour, self.rect)
