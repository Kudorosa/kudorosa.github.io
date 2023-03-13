#Test V
import pygame
from pygame.sprite import Sprite

class Ball(Sprite): 
    """ The Balls! """ 
    def __init__(self, screen, game_settings): 
        super(Ball, self).__init__()
        self.screen = screen 
        self.game_settings = game_settings
        
        #Alien Image
        self.image = pygame.image.load("C:/Users/Deand/Desktop/Alien_Invasion/"
                                                    "images/Crystal Ball.bmp")
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
        """ Checking if the Aliens hit a Screen Boundary and gives us True """ 
        screen_rect = self.screen.get_rect() 
        if self.rect.bottom >= screen_rect.bottom:
            return True 
        elif self.rect.top <= screen_rect.top: 
            return True
    
    def ball_hit(self, human):
        """ Checking to see if a Human hit a ball """
        if self.rect.bottom < human.rect.centerx:
            return True
    
    def update(self): 
        """ Allowing the Aliens to move """ 
        self.y += (self.game_settings.ball_speed * 
                                            self.game_settings.ball_direction)
        self.rect.y = self.y
