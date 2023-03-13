import pygame

class Settings(): 
    """ Settings for our Pygame! """ 
    def __init__(self): 
        """ Allowing for the Game Settings to work """ 
        self.screen_width = 975
        self.screen_height = 600
        self.bg_colour = (50,50,50)
        
        #Ranger & Target Speed.
        self.ranger_speed = 1
        self.target_drop_speed = 15
        
        #Directions (-1 = Left, 1 = Right).
        self.target_direction = 1
        
        #Lasers.
        self.laser_height = 4
        self.laser_width = 20
        self.laser_colour = 0, 255, 0
        self.capacity = 1
        
        #Tries Available
        self.shots_available = 3
        
        self.speedup = 1.25
        self.restore_settings()
    
    def restore_settings(self): 
        """ Restoring the Settings to the Default Values """ 
        #Target & Laser Speed
        self.target_speed = 0.5
        self.laser_speed = 1.5
    
    def increase_target_speed(self): 
        """ Increasing the Target Speed """ 
        self.laser_speed *= self.speedup
        self.target_speed *= self.speedup
