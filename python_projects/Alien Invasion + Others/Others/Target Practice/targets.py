#Test V
import pygame
from pygame.sprite import Sprite

class Target(Sprite): 
    """ The Targets! """ 
    def __init__(self, screen, game_settings): 
        super(Target, self).__init__()
        self.screen = screen 
        self.game_settings = game_settings
        
        #Target Image
        self.image = pygame.image.load("C:/Users/Deand/Desktop/Alien_Invasion/"
                                                            "images/Block.bmp")
        self.rect = self.image.get_rect() 
        
        #Position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x) 
        self.y = float(self.rect.y)
    
    def blitme(self): 
        """ """ 
        self.screen.blit(self.image, self.rect)
    
    def check_bounds(self): 
        """ Checking if the Targets hit a Screen Boundary and gives us True """ 
        screen_rect = self.screen.get_rect() 
        if self.rect.bottom >= screen_rect.bottom:
            return True 
        elif self.rect.top < screen_rect.top: 
            return True
    
    def update(self): 
        """ Allowing the Targets to move """ 
        self.y += (self.game_settings.target_speed * 
                                        self.game_settings.target_direction)
        self.rect.y = self.y
