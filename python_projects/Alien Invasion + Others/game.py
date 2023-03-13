import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from button import Button
from scoreboard import Scoreboard
from game_stats import GameStats

def run_game(): 
    """ Creating a Screen! """ 
    pygame.init() 
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, 
                                    game_settings.screen_height))
    stats = GameStats(game_settings) 
    sb = Scoreboard(game_settings, screen, stats) 
    
    pygame.display.set_caption("Return of the Aliens!") 
    play = Button(game_settings, screen, "PRESS PLAY!") 
    ship = Ship(screen, game_settings) 
    bg_colour = (game_settings.bg_colour)
    aliens = Group()
    bullets = Group()
    aliens_bullets = Group()
    gf.create_swarm(game_settings, screen, ship, aliens)
    """ Main Loop for the Game """
    while True: 
        gf.check_events(game_settings, stats, sb, screen, ship, aliens, 
                                                bullets, play, aliens_bullets) 
        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, stats, sb, ship, aliens, 
                                                    bullets, aliens_bullets)
            gf.update_aliens(game_settings, stats, sb, screen, ship, aliens, 
                                                    bullets, aliens_bullets)  
        gf.calibrate_screen(game_settings, stats, sb, screen, ship, aliens, 
                                                bullets , play, aliens_bullets) 
            
run_game() 
