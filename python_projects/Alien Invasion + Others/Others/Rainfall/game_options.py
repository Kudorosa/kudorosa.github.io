import pygame
import sys
from raindrops import Raindrop
from turrets import Turret


def get_number_rows(settings, helicopter_height, raindrop_height):
    """ Number of Rows for the Aliens """ 
    current_space_y = (settings.screen_height - 
                    (2 * raindrop_height) - helicopter_height)   
    number_rows = int(current_space_y / (3 * raindrop_height))
    return number_rows
    
def get_number_raindrops_x(settings, raindrop_width): 
    """ Getting the Number of Aliens """ 
    current_space_x = settings.screen_width - 1 * raindrop_width
    number_raindrops_x = int(current_space_x / (2 * raindrop_width)) 
    return number_raindrops_x

def create_raindrops(settings, screen, raindrops, raindrop_count, row_number): 
    """ Creating an Alien """ 
    raindrop = Raindrop(screen, settings)
    raindrop_width = raindrop.rect.width
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_count
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = (raindrop.rect.height + 2 * 
                                            raindrop.rect.height * row_number)   
    raindrops.add(raindrop) 

def spawn_rain(settings, screen, helicopter, raindrops):
    """ Creating a Swarm of Aliens """ 
    #Spacing between Aliens is equal to one Alien Width.
    raindrop = Raindrop(screen, settings) 
    number_raindrops_x = get_number_raindrops_x(settings, raindrop.rect.width)
    number_rows = get_number_rows(settings, helicopter.rect.height, 
                                                raindrop.rect.height)
    
    #Creating the First Row of Aliens. 
    for row_number in range(number_rows):
        for raindrop_count in range(number_raindrops_x): 
            create_raindrops(settings, screen, raindrops, raindrop_count, 
                                                                    row_number)

def check_rain_bounds(settings, raindrops):
    """ Checking the Bounds of the Rain """ 
    for raindrop in raindrops.sprites(): 
        if raindrop.rain_bounds(): 
            rainfall(settings, raindrops)
            break

def rainfall(settings, raindrops): 
    """ Unleashing the Rain """ 
    for raindrop in raindrops.sprites():
        raindrop.rect.y += settings.rain_drop_speed
    settings.rain_direction *= -1

def update_rain(settings, screen, helicopter, raindrops):
    """ Updating the Rain """ 
    check_rain_bounds(settings, raindrops)
    for raindrop in raindrops.sprites(): 
        if raindrop.rain_bounds() == False:
            raindrops.remove(raindrop)
        if raindrop not in raindrops.sprites():
            spawn_rain(settings, screen, helicopter, raindrops)
            break
        break
    raindrops.update()
            
        

def keypress(event, settings, screen, helicopter, turrets): 
    """ Any Specific Key Pressed will Activate an Event """
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        helicopter.shift_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        helicopter.shift_left = True 
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        helicopter.ascend = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        helicopter.descend = True
    elif event.key == pygame.K_SPACE:
        engage(settings, screen, helicopter, turrets)
    elif event.key == pygame.K_q: 
        sys.exit() 

def engage(settings, screen, helicopter, turrets): 
    """ """ 
    if len(turrets) < settings.limit:
        new_turret = Turret(settings, screen, helicopter) 
        turrets.add(new_turret) 
    

def key_released(event, helicopter, turrets):
    """ Stopping any Events once a Key is no longer Pressed """ 
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        helicopter.shift_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        helicopter.shift_left = False
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        helicopter.ascend = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s: 
        helicopter.descend = False
                
def event_check(settings, screen, helicopter, turrets):
    """ Checking for any Events """ 
    for event in pygame.event.get():
        if event == "QUIT":
            sys.exit() 
    
        elif event.type == pygame.KEYDOWN:
            keypress(event, settings, screen, helicopter, turrets) 
            
        elif event.type == pygame.KEYUP:
            key_released(event, helicopter, turrets) 


def refresh_screen(settings, screen, helicopter, raindrops, turrets): 
    """ Screen Refresh """ 
    pygame.display.flip() 
    screen.fill(settings.screen_colour)
    helicopter.blitme()
    raindrops.draw(screen) 
    for turret in turrets.sprites():
        turret.draw_bullets()

def erasing_bullets(turrets): 
    """ Getting Rid of Expended Missles """ 
    turrets.update() 
    for turret in turrets.copy():
        if turret.rect.left <= 0: 
            turrets.remove(turret) 
     


