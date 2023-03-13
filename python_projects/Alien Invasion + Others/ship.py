import pygame
from pygame.sprite import Sprite
class Ship(Sprite): 
    """ The Class containing a Ships and it's Behaviour """ 
    def __init__(self, screen, game_settings): 
        """ Initialize the Ship and it's Start Position """ 
        super(Ship, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        
        
        #Loading the Ship and gettings it's Rect(angle). 
        self.image = pygame.image.load("images/Ship.bmp") 
        self.rect = self.image.get_rect() 
        self.screen_rect = self.screen.get_rect() 
        
        #Starts each Ship at the Bottom of the Screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx) 
        self.bottom = float(self.rect.bottom) 
       
        #Movement 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def blitme(self): 
        """ Draw the Ship at the Current Location """ 
        self.screen.blit(self.image, self.rect) 
    
    def center_ship(self):
        """ Centering the Ship """ 
        self.bottom = self.screen_rect.bottom
    
    def update(self):
        """ Movement for the Ship """ 
        if self.moving_right == True:
            #Boundaries. 
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.game_settings.ship_speed  
        
        if self.moving_left == True:
            if self.moving_left and self.rect.left > 0:
                self.center -= self.game_settings.ship_speed 
        
        if self.moving_up == True: 
            if self.moving_up and self.rect.top > self.screen_rect.top:
                self.bottom -= self.game_settings.ship_speed 
        
        if self.moving_down == True:
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.bottom += self.game_settings.ship_speed 
        
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom































