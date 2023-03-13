import pygame

class Settings(): 
    """ Settings for our Pygame! """ 
    def __init__(self): 
        """ Allowing for the Game Settings to work """ 
        self.screen_width = 975
        self.screen_height = 600
        self.bg_colour = (25,25,25)
        
        #Ship & Alien Speed.
        self.ship_speed = 5
        self.ball_speed = 0.5
        #Directions (-1 = Left, 1 = Right).
        self.ball_direction = 1
        
        #Bullets.
        self.bullet_speed = 1.8
        self.bullet_height = 20
        self.bullet_width = 3
        self.bullet_colour = 250, 0, 50
        self.capacity = 2
        
        #Attempts
        self.tries_remaining = 3
