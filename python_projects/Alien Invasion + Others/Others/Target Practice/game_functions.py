from time import sleep
import pygame 
import sys
from targets import Target
from lasers import Laser



def ranger_missed(game_settings, stats, screen, ranger, targets, lasers): 
    """ Detecting if the Ranger was Hit """ 
    #Takeaway one Ranger from the Ranger Availability. 
    stats.shots_left -= 1 
    if stats.shots_left > 0:
    
        #Empty the List of Targets and Lasers.
        targets.empty()
        lasers.empty()
    
        create_targets(game_settings, screen, ranger, targets)
        ranger.center_ranger() 
    
        sleep(0.05) 
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def create_targets(game_settings, screen, ranger, targets): 
    """ Creating an Target """ 
    target = Target(screen, game_settings)
    targets.add(target) 
 
def check_target_bounds(game_settings, targets):
    """ Checking the Swarm's Edges """
    for target in targets.sprites():
        if target.check_bounds(): 
            redirect_target(game_settings, targets)
            break

def redirect_target(game_settings, targets): 
    """ Drop and Redirect the Swarm """ 
    for target in targets.sprites():
        target.rect.y += game_settings.target_drop_speed
    game_settings.target_direction *= -1
    
def update_targets(game_settings, stats, screen, ranger, targets, lasers):
    """ Updating the Targets so they can move
    and checking if they are at the Edge of the Screen """ 
    check_target_bounds(game_settings, targets) 
    targets.update() 
    
    if pygame.sprite.spritecollideany(ranger, targets):
        ranger_missed(game_settings, stats, screen, ranger, targets, lasers)
        

        

def keyup_event(event, game_settings, screen, ranger, lasers):
    """ Checking for Keyup Events """ 
    #Left and Right Controls Release.
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ranger.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ranger.moving_left = False
            
    #Up and Down Controls Release.    
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ranger.moving_up = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ranger.moving_down = False
    
        
def keydown_event(event, game_settings, screen, ranger, lasers, stats, play, 
    targets):
    """ Checking for Keydown Events. """ 
    #Left and Right Controls.
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ranger.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ranger.moving_left = True
                
    #Up and Down Controls.    
    elif event.key == pygame.K_UP or event.key == pygame.K_w: 
        ranger.moving_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ranger.moving_down = True
        
    #Shooting.
    elif event.key == pygame.K_SPACE:
        shoot(game_settings, screen, ranger, lasers)      
    
    #Quit & Restarts
    elif event.key == pygame.K_q: 
        sys.exit()
        
    elif event.key == pygame.K_p:
        start_game(game_settings, screen, stats, play, ranger, targets, lasers, 
                                                                        event)
        
        
def mouse_event(event, game_settings, screen, ranger, lasers):
    """ Mouse Controls """ 
    #Shooting Controls. 
    if event.button == 1:
        shoot(game_settings, screen, ranger, lasers)
        
def shoot(game_settings, screen, ranger, lasers):
    """ Shoot Now! """ 
    if len(lasers) < game_settings.capacity:
        new_laser = Laser(game_settings, screen, ranger) 
        lasers.add(new_laser) 

    
        
def check_events(game_settings, stats, screen, ranger, targets, lasers, play):
    """ Allows for the Checking of Player Inputs """ 
    for event in pygame.event.get():
        if event == "QUIT":
            sys.exit() 
            
            """ Keyboard & Mouse Events """
        elif event.type == pygame.KEYDOWN:
            keydown_event(event, game_settings, screen, ranger, lasers, stats, 
                                                                play, targets)
            if event.key == pygame.K_p:
                start_game(game_settings, screen, stats, play, ranger, targets,
                                                            lasers, event)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_event(event, game_settings, screen, ranger, lasers)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play(game_settings, screen, stats, play, ranger, targets, 
                                                    lasers, mouse_x, mouse_y)
        
        elif event.type == pygame.KEYUP:
            keyup_event(event, game_settings, screen, ranger, lasers)
            

def check_play(game_settings, screen, stats, play, ranger, targets, lasers,
                                                        mouse_x, mouse_y):
    """ Checking to see if the Play Button was pressed """ 
    button_clicked = play.rect.collidepoint(mouse_x, mouse_y)
    if stats.game_active == False and button_clicked:
        game_settings.restore_settings()
        pygame.mouse.set_visible(False)
        #Resetting the Game.
        stats.reset_stats()
        stats.game_active = True
        
        targets.empty()
        lasers.empty() 
        
        create_targets(game_settings, screen, ranger, targets)
        ranger.center_ranger() 

def start_game(game_settings, screen, stats, play, ranger, targets, lasers,  
    event):
    """ """ 
    if stats.game_active == False:
        game_settings.restore_settings()
        pygame.mouse.set_visible(False)
        #Resetting the Game.
        stats.reset_stats()
        stats.game_active = True
        
        targets.empty()
        lasers.empty() 
        
        create_targets(game_settings, screen, ranger, targets)
        ranger.center_ranger() 
            
        
def calibrate_screen(game_settings, stat, screen, ranger, targets, lasers, play): 
    """ """ 
    """ Allowing for the Screen to be constantly updated """ 
    screen.fill(game_settings.bg_colour)
    targets.draw(screen)
    ranger.blitme()
    for laser in lasers.sprites():
        laser.draw_laser()
    if not stat.game_active:
        play.draw_button() 
    pygame.display.flip() 
   
def update_lasers(game_settings, screen, ranger, targets, lasers, stats):
    """ """ 
    lasers.update() 
    
    for laser in lasers.copy(): 
        if laser.rect.right <= 0: 
            ranger_missed(game_settings, stats, screen, ranger, targets, lasers)
            lasers.remove(laser)
    check_target_hit(game_settings, screen, ranger, targets, lasers)
       
       
def check_target_hit(game_settings, screen, ranger, targets, lasers):
    """ Check to see if any Target(s) were hit by Laser(s) """ 
     #Checking for any Lasers that hit an Target.
    collisions = pygame.sprite.groupcollide(lasers, targets, True, True)
    if len(targets) == 0:
        lasers.empty
        game_settings.increase_target_speed()
        create_targets(game_settings, screen, ranger, targets) 
