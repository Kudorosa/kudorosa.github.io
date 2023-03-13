import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite): 
    """ Making a Class of Stars! """ 
    def __init__(self, screen, settings):
        super(Raindrop, self).__init__() 
        self.screen = screen
        self.settings = settings
    
        self.image = pygame.image.load("C:/Users/Deand/Desktop/Alien_Invasion/"
                                                        "images/Raindrop.bmp") 
        self.rect = self.image.get_rect() 
    
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
        self.x = float(self.rect.x) 
    
    def rain_bounds(self):
        """ Rain Bounds """ 
        screen_rect = self.screen.get_rect() 
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        elif self.rect.bottom >= screen_rect.bottom:
            return False
    
    def update(self): 
        """ Updating the Rain Movement """ 
        self.x += (self.settings.rain_speed * self.settings.rain_direction)
        
        self.rect.x = self.x
    
    def blitme(self):
        """ """ 
        self.screen.blit(self.image, self.rect) 
