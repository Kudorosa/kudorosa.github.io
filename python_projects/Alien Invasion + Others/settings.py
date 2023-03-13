import pygame

class Settings(): 
    """ Settings for our Pygame! """ 
    def __init__(self): 
        """ Allowing for the Game Settings to work """ 
        self.screen_width = 975
        self.screen_height = 600
        self.bg_colour = (0,50,100)
        
        #Bullets.
        self.bullet_height = 20
        self.bullet_width = 3
        self.bullet_colour = 250, 0, 50
        self.capacity = 2
        
        #Alien Bullets.
        self.alien_bullet_height = 10
        self.alien_bullet_width = 2
        self.alien_bullet_colour = 40, 250, 60
        
        #Alien Dropspeed
        self.swarm_drop_speed = 15
        
        #Ship Availability.
        self.ships_available = 3
        
        
        #Game Speedup 
        self.boost_alien_bullet = 1.05
        self.speed_boost = 1.10
        self.score_multiplier = 1.5
        self.implement_dynamic_settings() 
        
    def implement_dynamic_settings(self):
        """ Implementing the Settings """ 
        #Bullet Speed
        self.bullet_speed = 1.5
        self.alien_bullet_speed = 0.5
            
        #Ship & Alien Speed.
        self.ship_speed = 0.5
        self.swarm_speed = 1
        
        #Directions (-1 = Left, 1 = Right).
        self.swarm_direction = 1
        
        #Alien Score.
        self.alien_points = 25
    
    def increase_difficulty(self):
        """ Increasing the Difficulty of the Game """ 
        self.alien_bullet_speed *= self.boost_alien_bullet
        self.bullet_speed *= self.speed_boost
        self.ship_speed *= self.speed_boost
        self.swarm_speed *= self.speed_boost
        self.alien_points = int(self.alien_points * self.score_multiplier)
       
        
