#TEST V------------------------------------------------
import pygame
import sys

class Option(): 
    """ Options for the Game """ 
    def __init__(self):
        self.screen_width = 975
        self.screen_height = 600
        self.screen_colour = (10,10,30) 
        
        #Rocket Speed
        self.rocket_speed = 1
        
        #Missles
        self.missle_speed = 4
        self.missle_height = 8
        self.missle_width = 100
        self.missle_colour = 250, 250, 150
        self.limit = 2
    



