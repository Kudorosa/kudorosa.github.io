import pygame
import sys
from stars import Star
from missles import Missle
from random import randint

def get_number_rows(options, rocket_height, star_height):
    """ Number of Rows for the Aliens """ 
    current_space_y = (options.screen_height - 
                    (1.5 * star_height) - rocket_height)   
    number_rows = int(current_space_y / (1.5 * star_height))
    return number_rows
    
def get_number_stars_x(options, star_width): 
    """ Getting the Number of Aliens """ 
    current_space_x = options.screen_width - 1 * star_width
    number_stars_x = int(current_space_x / (2 * star_width)) 
    return number_stars_x

def create_stars(options, screen, stars, star_count, row_number): 
    """ Creating an Alien """ 
    star = Star(screen, options)
    star_width = star.rect.width
    star.x = star_width + 4 * star_width * star_count
    star.rect.x = star.x
    random_number = randint(1, 5)
    star.rect.y = star.rect.height + random_number * star.rect.height * row_number
    stars.add(star) 

def summon_constellation(options, screen, rocket, stars):
    """ Creating a Swarm of Aliens """ 
    #Spacing between Aliens is equal to one Alien Width.
    star = Star(screen, options) 
    number_stars_x = get_number_stars_x(options, star.rect.width)
    number_rows = get_number_rows(options, rocket.rect.height, 
                                                star.rect.height)
    
    #Creating the First Row of Aliens. 
    for row_number in range(number_rows):
        for star_count in range(number_stars_x): 
            create_stars(options, screen, stars, star_count, row_number)

def keypress(event, options, screen, rocket, missles): 
    """ Any Specific Key Pressed will Activate an Event """
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        rocket.shift_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        rocket.shift_left = True 
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        rocket.ascend = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        rocket.descend = True
    elif event.key == pygame.K_SPACE:
        engage(options, screen, rocket, missles)
    elif event.key == pygame.K_q: 
        sys.exit() 

def engage(options, screen, rocket, missles): 
    """ """ 
    if len(missles) < options.limit:
        new_missle = Missle(options, screen, rocket) 
        missles.add(new_missle) 
    

def key_released(event, rocket, missles):
    """ Stopping any Events once a Key is no longer Pressed """ 
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        rocket.shift_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        rocket.shift_left = False
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        rocket.ascend = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s: 
        rocket.descend = False
                
def event_check(options, screen, rocket, missles):
    """ Checking for any Events """ 
    for event in pygame.event.get():
        if event == "QUIT":
            sys.exit() 
    
        elif event.type == pygame.KEYDOWN:
            keypress(event, options, screen, rocket, missles) 
            
        elif event.type == pygame.KEYUP:
            key_released(event, rocket, missles) 


def refresh_screen(options, screen, rocket, stars, missles): 
    """ Screen Refresh """ 
    pygame.display.flip() 
    screen.fill(options.screen_colour)
    rocket.blitme()
    stars.draw(screen) 
    for missle in missles.sprites():
        missle.draw_missle()

def erasing_missles(missles): 
    """ Getting Rid of Expended Missles """ 
    missles.update() 
    for missle in missles.copy():
        if missle.rect.left <= 0: 
            missles.remove(missle) 
     


