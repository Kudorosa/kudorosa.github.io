import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard(): 
    """ A Class Representing a Scoreboard which will Record Scores. """ 
    def __init__(self, game_settings, screen, stats): 
        """ """ 
        self.screen = screen
        self.screen_rect = screen.get_rect() 
        self.game_settings = game_settings
        self.stats = stats

        #Font Settings for Scoreboard. 
        self.text_colour = (40, 250, 60)
        self.score_text_colour = (250, 250, 250)
        self.level_text_colour = (250, 0, 0)
        self.font = pygame.font.SysFont(None, 46) 
        
        self.prep_images()
        
    def prep_images(self): 
        """Preparing the Score Image. """
        self.prep_score() 
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        """ The Score """ 
        rounded_score = int(round(self.stats.score, - 1)) #round() rounds Numbers to the nearest Interger which is specified, -1 ensure Numbers are Multiples of 10. 
        score_str = "{:,}".format(rounded_score)  
        self.score_image = self.font.render(score_str, True, self.text_colour, 
                                        self.game_settings.bg_colour)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        """ The High Score """ 
        rounded_high_score = int(round(self.stats.high_score, - 1))
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, 
                        self.score_text_colour, self.game_settings.bg_colour)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        """ The Level which is presented """ 
        self.level_image = self.font.render(str(self.stats.level), True, 
                                self.level_text_colour, 
                                                self.game_settings.bg_colour)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        """ Preparing the Number of Ships the Player has left """ 
        self.ships = Group() 
        for number_of_ships in range(self.stats.ships_left):
            ship = Ship(self.screen, self.game_settings) 
            ship.rect.x = 10 + number_of_ships * ship.rect.width #10 Pixels away from the Left Side.
            ship.rect.y = 10 #10 Pixels down from the Top of the Screen.
            self.ships.add(ship)
        
        
    def show_score(self):
        """ Displaying the Score """ 
        self.screen.blit(self.score_image, self.score_rect) 
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        
