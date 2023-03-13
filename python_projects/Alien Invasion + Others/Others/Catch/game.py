import pygame
from pygame.sprite import Group
from settings import Settings
from human import Human
import game_functions as gf
from statistic import Statistics

def run_game(): 
    """ Creating a Screen! """ 
    pygame.init() 
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, 
                                    game_settings.screen_height))
    pygame.display.set_caption("Catch!") 
    human = Human(screen, game_settings) 
    bg_colour = (game_settings.bg_colour)
    balls = Group()
    bullets = Group()
    stat = Statistics(game_settings)
    gf.create_barrage(game_settings, screen, human, balls)
    """ Main Loop for the Game """
    while True: 
        gf.check_events(game_settings, screen, human, bullets) 
        if stat.game_ongoing:
            human.update()
            gf.update_bullets(game_settings, screen, human, balls, bullets)
            gf.update_balls(game_settings, stat, screen, human, balls, bullets)  
        gf.calibrate_screen(game_settings, screen, human, balls, bullets) 
        
run_game() 
