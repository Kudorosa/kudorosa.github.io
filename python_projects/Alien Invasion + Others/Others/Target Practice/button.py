import pygame.font 

class Button(): 
    
    def __init__(self, game_settings, screen, msg):
        """ """ 
        self.screen = screen
        self.screen_rect = screen.get_rect() 
        
        #Dimensions and Properties of the Button. 
        self.width, self.height = 200, 50
        self.button_colour = (100,100,100)  
        self.text_colour = (255,255,255) 
        self.font = pygame.font.SysFont(None, 42)
        
        #Building the Button Rect and Centering it. 
        self.rect = pygame.Rect(0,0, self.width, self.height) 
        self.rect.center = self.screen_rect.center
        
        #Preparing the Button Once. 
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        """ Allowing the Message to be Rendered into an Image. """ 
        self.msg_image = self.font.render(msg, True, self.text_colour, 
                                                    self.button_colour) 
        self.msg_image_rect = self.msg_image.get_rect() 
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self): 
        """ Allowing the Button to be displayed """ 
        self.screen.fill(self.button_colour, self.rect) 
        self.screen.blit(self.msg_image, self.msg_image_rect) 
        
