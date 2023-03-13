import pygame
from pygame.sprite import Group
from settings import Settings
from ranger import Ranger
import game_functions as gf
from button import Button
from game_stats import GameStats

def run_game(): 
    """ Creating a Screen! """ 
    pygame.init() 
    game_settings = Settings()
    stats = GameStats(game_settings) 
    screen = pygame.display.set_mode((game_settings.screen_width, 
                                    game_settings.screen_height))
    pygame.display.set_caption("Return of the Targets!") 
    play = Button(game_settings, screen, "PRESS PLAY!") 
    ranger = Ranger(screen, game_settings) 
    bg_colour = (game_settings.bg_colour)
    blocks = Group()
    lasers = Group()
    gf.create_targets(game_settings, screen, ranger, blocks)
    """ Main Loop for the Game """
    while True: 
        gf.check_events(game_settings, stats, screen, ranger, blocks, lasers, 
                                play) 
        if stats.game_active:
            ranger.update()
            gf.update_lasers(game_settings, screen, ranger, blocks, lasers, 
                                stats)
            gf.update_targets(game_settings, stats, screen, ranger, blocks, 
                                                                    lasers)  
        gf.calibrate_screen(game_settings, stats, screen, ranger, blocks, 
                                lasers, play) 
            
run_game() 
