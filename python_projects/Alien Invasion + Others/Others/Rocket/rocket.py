#TEST V---------------------------------------------------------------------------
import pygame

class Rocket(): 
    """ A Rocket that has Advanced Maneouverability. """ 
    def __init__(self, screen, options):
        """ """ 
        self.screen = screen
        self.options = options
        
        self.image = pygame.image.load("C:/Users/Deand/Desktop/Alien_Invasion/"
                                                "images/Horizontal Rocket.bmp") 
        self.rect = self.image.get_rect() 
        self.screen_rect = self.screen.get_rect() 
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.center = float(self.rect.centerx) 
        self.bottom = float(self.rect.bottom)
        
        self.shift_right = False
        self.shift_left = False
        self.ascend = False
        self.descend = False
    
    def movement(self): 
        """ Movement for the Rocket to Maneouver """ 
        if self.shift_right == True:
            if self.shift_right and self.rect.right < self.screen_rect.right:
                self.center += self.options.rocket_speed
        if self.shift_left == True:
            if self.shift_left and self.rect.left > 0:
                self.center -= self.options.rocket_speed 
        if self.ascend == True:
            if self.ascend and self.rect.top > self.screen_rect.top:
                self.bottom -= self.options.rocket_speed 
        if self.descend == True:
            if self.descend and self.rect.bottom < self.screen_rect.bottom:
                self.bottom += self.options.rocket_speed
                
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom
     
     
     
     
        
    def blitme(self):
        """ The Rocket """ 
        self.screen.blit(self.image, self.rect) 
        
