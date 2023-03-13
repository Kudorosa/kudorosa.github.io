import pygame
from pygame.sprite import Sprite

class Star(Sprite): 
    """ Making a Class of Stars! """ 
    def __init__(self, screen, options):
        super(Star, self).__init__() 
        self.screen = screen
        self.options = options
    
        self.image = pygame.image.load("C:/Users/Deand/Desktop/Alien_Invasion/"     
                                                            "images/Star.bmp") 
        self.rect = self.image.get_rect() 
    
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
        self.x = float(self.rect.x) 
    
    def blitme(self):
        """ """ 
        self.screen.blit(self.image, self.rect) 
