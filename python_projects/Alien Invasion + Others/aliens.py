#Test V
import pygame
from pygame.sprite import Sprite

class Alien(Sprite): 
    """ The Aliens! """ 
    def __init__(self, screen, game_settings): 
        super(Alien, self).__init__()
        self.screen = screen 
        self.game_settings = game_settings
        
        #Alien Image
        self.image = pygame.image.load("images/Alien.bmp")
        self.rect = self.image.get_rect() 
        
        #Position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x) 
    
    def blitme(self): 
        """ """ 
        self.screen.blit(self.image, self.rect)
    
    def check_bounds(self): 
        """ Checking if the Aliens hit a Screen Boundary and gives us True """ 
        screen_rect = self.screen.get_rect() 
        if self.rect.right >= screen_rect.right:
            return True 
        elif self.rect.left <= 0: 
            return True
    
    def update(self): 
        """ Allowing the Aliens to move """ 
        self.x += (self.game_settings.swarm_speed * 
                                            self.game_settings.swarm_direction)
        self.rect.x = self.x
