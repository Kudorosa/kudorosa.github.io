#TEST V------------------------------------------------
import pygame
import sys

class Setting(): 
    """ Options for the Game """ 
    def __init__(self):
        self.screen_width = 975
        self.screen_height = 600
        self.screen_colour = (10,10,30) 
        
        #Helicopter Speed
        self.helicopter_speed = 1
        
        #Bullets
        self.bullets_speed = 4
        self.bullets_height = 8
        self.bullets_width = 100
        self.bullets_colour = 250, 250, 150
        self.limit = 5
        
        self.rain_speed = 0.5
        self.rain_drop_speed = 40 
        self.rain_direction = -1
        



