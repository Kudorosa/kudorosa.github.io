import pygame
        
class Ranger(): 
    """ The Class containing a Rangers and it's Behaviour """ 
    def __init__(self, screen, game_settings): 
        """ Initialize the Ranger and it's Start Position """ 
        self.screen = screen
        self.game_settings = game_settings
        
        self.image = pygame.image.load("C:/Users/Deand/Desktop/Alien_Invasion/"
                                                "images/Ranger.bmp") 
        self.rect = self.image.get_rect() 
        self.screen_rect = self.screen.get_rect() 
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.center = float(self.rect.centerx) 
        self.bottom = float(self.rect.bottom)
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
        
    def blitme(self): 
        """ Draw the Ranger at the Current Location """ 
        self.screen.blit(self.image, self.rect) 
    
    def center_ranger(self):
        """ Centering the Ranger """ 
        self.bottom = self.screen_rect.bottom
    
    def update(self):
        """ Movement for the Ranger """ 
        if self.moving_right == True:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.game_settings.ranger_speed  
        
        if self.moving_left == True:
            if self.moving_left and self.rect.left > 0:
                self.center -= self.game_settings.ranger_speed 
        
        if self.moving_up == True: 
            if self.moving_up and self.rect.top > self.screen_rect.top:
                self.bottom -= self.game_settings.ranger_speed 
        
        if self.moving_down == True:
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.bottom += self.game_settings.ranger_speed 
        
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom






























