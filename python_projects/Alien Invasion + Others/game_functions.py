from time import sleep
import json
import pygame 
import sys
from aliens import Alien
from bullets import Bullet
from aliens_bullets import AlienBullet
import pygame.mixer 
pygame.mixer.init()

def music(stats):
    """ Music to be played """ 
    if stats.game_active == True:
        pygame.mixer.music.load("Music/puredesigngirl.mp3")
        pygame.mixer.music.play(-1)
    elif stats.game_active == False:
        pygame.mixer.music.stop()
   
    

def ship_hit(game_settings, stats, sb, screen, ship, aliens, bullets, 
aliens_bullets): 
    """ Detecting if the Ship was Hit """ 
    #Takeaway one Ship from the Ship Availability. 
    dmg = pygame.mixer.Sound("Sounds/damage.wav")
    pygame.mixer.Sound.play(dmg)
    stats.ships_left -= 1 
    sb.prep_ships()
    if stats.ships_left > 0:
        #Update the Amount of Ships that are Displayed. 
        sb.prep_ships()
    
        #Empty the List of Aliens and Bullets.
        reset_level(game_settings, screen, stats, sb, ship, aliens, bullets,
        aliens_bullets)
    
        sleep(0.3) 
    else:
        lose = pygame.mixer.Sound("Sounds/over.wav") 
        pygame.mixer.Sound.play(lose)
        stats.game_active = False
        music(stats)
        pygame.mouse.set_visible(True)

def check_alien_bottoms(game_settings, stats, sb, screen, ship, aliens, 
bullets, aliens_bullets):
    """ Detecting if the Alien is at the Bottom of the Screen """ 
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Treating it as if the Ship were hit. 
            ship_hit(game_settings, stats, sb, screen, ship, aliens, bullets, 
            aliens_bullets)
            break
    
def get_number_rows(game_settings, ship_height, alien_height):
    """ Number of Rows for the Aliens """ 
    current_space_y = (game_settings.screen_height - 
                    (3 * alien_height) - ship_height)   
    number_rows = int(current_space_y / (2 * alien_height))
    return number_rows
    
def get_number_aliens_x(game_settings, alien_width): 
    """ Getting the Number of Aliens """ 
    current_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(current_space_x / (2 * alien_width)) 
    return number_aliens_x

def create_aliens(game_settings, screen, aliens, alien_count, row_number): 
    """ Creating an Alien """ 
    alien = Alien(screen, game_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_count
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien) 

def create_swarm(game_settings, screen, ship, aliens):
    """ Creating a Swarm of Aliens """ 
    #Spacing between Aliens is equal to one Alien Width.
    alien = Alien(screen, game_settings) 
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, 
                                                        alien.rect.height)
    
    #Creating the First Row of Aliens. 
    for row_number in range(number_rows):
        for alien_count in range(number_aliens_x): 
            create_aliens(game_settings, screen, aliens, alien_count, 
                                                                    row_number) 

def check_swarm_bounds(game_settings, aliens, stats, screen, sb, ship, 
aliens_bullets):
    """ Checking the Swarm's Edges """
    for alien in aliens.sprites():
        if alien.check_bounds(): 
            redirect_swarm(game_settings, aliens, stats, screen, sb, ship, 
            aliens_bullets)
            break

def redirect_swarm(game_settings, aliens, stats, screen, sb, ship, 
aliens_bullets): 
    """ Drop and Redirect the Swarm """ 
    for alien in aliens.sprites():
        alien.rect.y += game_settings.swarm_drop_speed
    game_settings.swarm_direction *= -1
    aliens_shoot(game_settings, stats, screen, ship, aliens_bullets, aliens)
    
def update_aliens(game_settings, stats, sb, screen, ship, aliens, bullets, 
aliens_bullets):
    """ Updating the Aliens so they can move
    and checking if they are at the Edge of the Screen """ 
    check_swarm_bounds(game_settings, aliens, stats, screen, sb, ship, 
aliens_bullets)
    aliens.update() 
    
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, stats, sb, screen, ship, aliens, bullets, 
            aliens_bullets)
    check_alien_bottoms(game_settings, stats, sb, screen, ship, aliens, 
                                                    bullets, aliens_bullets)
        

def keyup_event(event, game_settings, screen, ship, bullets):
    """ Checking for Keyup Events """ 
    #Left and Right Controls Release.
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
            
    #Up and Down Controls Release.    
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = False
    
        
def keydown_event(event, game_settings, screen, ship, bullets, stats, play, 
    aliens):
    """ Checking for Keydown Events. """ 
    #Left and Right Controls.
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
                
    #Up and Down Controls.    
    elif event.key == pygame.K_UP or event.key == pygame.K_w: 
        ship.moving_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = True
        
    #Shooting.
    elif event.key == pygame.K_SPACE:
        shoot(game_settings, screen, ship, bullets)      
    
    #Quit & Restarts
    elif event.key == pygame.K_q: 
        score = "Alien Invasion High-Score.txt"
        try:
            with open(score) as file_object:
                high_score = file_object.readlines()
                for hs in high_score:
                    if stats.high_score > int(hs):
                        hs = round(stats.high_score, -1)
                        with open(score, "w") as file_object:
                            json.dump(hs, file_object)
                    else:
                        break
                
        except FileNotFoundError: 
            with open(score, "w") as file_object:
                score = round(stats.high_score, -1)
                file_object.write(str(score))
        
        sys.exit()
        
    elif event.key == pygame.K_p:
        start_game(game_settings, screen, stats, play, ship, aliens, bullets, 
                                                                        event)
        
        
def mouse_event(event, game_settings, screen, ship, bullets):
    """ Mouse Controls """ 
    #Shooting Controls. 
    if event.button == 1:
        shoot(game_settings, screen, ship, bullets)
        
def shoot(game_settings, screen, ship, bullets):
    """ Shoot Now! """ 
    if len(bullets) < game_settings.capacity:
        new_bullet = Bullet(game_settings, screen, ship) 
        bullets.add(new_bullet) 
        blast = pygame.mixer.Sound("Sounds/laser.wav")
        pygame.mixer.Sound.play(blast)

def aliens_shoot(game_settings, stats, screen, ship, aliens_bullets, aliens):
    """ Aliens will Shoot! """ 
    if stats.level > 1 and len(aliens) < 7:
        a_bullet = AlienBullet(game_settings, screen, aliens) 
        aliens_bullets.add(a_bullet) 
        blast = pygame.mixer.Sound("Sounds/level.wav")
        pygame.mixer.Sound.play(blast)

    
        
def check_events(game_settings, stats, sb, screen, ship, aliens, bullets, 
play, aliens_bullets):
    """ Allows for the Checking of Player Inputs """ 
    for event in pygame.event.get():
        if event == "QUIT":
            sys.exit() 
            
            """ Keyboard & Mouse Events """
        elif event.type == pygame.KEYDOWN:
            keydown_event(event, game_settings, screen, ship, bullets, stats, 
                                                                play, aliens)
            if event.key == pygame.K_p:
                start_game(game_settings, screen, stats, play, ship, aliens,
                                                            bullets, event)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_event(event, game_settings, screen, ship, bullets)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play(game_settings, screen, stats, sb, play, ship, aliens, 
                                    bullets, mouse_x, mouse_y, aliens_bullets)
        
        elif event.type == pygame.KEYUP:
            keyup_event(event, game_settings, screen, ship, bullets)
            

def check_play(game_settings, screen, stats, sb, play, ship, aliens, bullets,
                                            mouse_x, mouse_y, aliens_bullets):
    """ Checking to see if the Play Button was pressed """ 
    button_clicked = play.rect.collidepoint(mouse_x, mouse_y)
    if stats.game_active == False and button_clicked:
        game_settings.implement_dynamic_settings()
        pygame.mouse.set_visible(False)
        #Resetting the Game.
        stats.reset_stats()
        stats.game_active = True
        
        sb.prep_images()
        reset_level(game_settings, screen, stats, sb, ship, aliens, bullets, 
        aliens_bullets)
        music(stats)
        

def reset_level(game_settings, screen, stats, sb, ship, aliens, bullets, 
aliens_bullets):
    """ Resetting the Level """ 
    aliens.empty()
    bullets.empty() 
    aliens_bullets.empty()

    create_swarm(game_settings, screen, ship, aliens)
    ship.center_ship() 

def start_game(game_settings, screen, stats, play, ship, aliens, bullets,  
    event):
    """ """ 
    if stats.game_active == False:
        game_settings.implement_dynamic_settings()
        pygame.mouse.set_visible(False)
        #Resetting the Game.
        stats.reset_stats()
        lose = pygame.mixer.Sound("Sounds/over.wav") 
        pygame.mixer.Sound.play(lose)
        stats.game_active = True
        
        reset_level(game_settings, screen, stats, sb, play, ship, aliens, 
        bullets)
        

def check_high_score(stats, sb):
    """ Checking for a High Score """ 
    sb.prep_high_score()
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
            
        
def calibrate_screen(game_settings, stat, sb, screen, ship, aliens, bullets, 
play, aliens_bullets): 
    """ """ 
    """ Allowing for the Screen to be constantly updated """ 
    screen.fill(game_settings.bg_colour)
    aliens.draw(screen)
    ship.blitme()
    sb.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    for bullet1 in aliens_bullets.sprites():
        bullet1.draw_bullet()
        
    if not stat.game_active:
        play.draw_button() 
    pygame.display.flip() 
   
def update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets, 
aliens_bullets):
    """ """ 
    bullets.update() 
    aliens_bullets.update()
    
    for bullet in bullets.copy(): 
        if bullet.rect.bottom <= 0: 
            bullets.remove(bullet)
    check_alien_hit(game_settings, screen, stats, sb, ship, aliens, bullets,
     aliens_bullets)
    
    for bullet in aliens_bullets.copy(): 
        if bullet.rect.top <= 0: 
            aliens_bullets.remove(bullet)
    check_ship_hit(game_settings, screen, stats, sb, ship, aliens, bullets, 
    aliens_bullets)
       
       
def check_alien_hit(game_settings, screen, stats, sb, ship, aliens, bullets, 
aliens_bullets):
    """ Check to see if any Alien(s) were hit by Bullet(s) """ 
     #Checking for any Bullets that hit an Alien, and Increasing the Difficulty
     #once all Aliens have been Vanquished.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    for aliens in collisions.values():
        stats.score += game_settings.alien_points * len(aliens)
        boom = pygame.mixer.Sound("Sounds/explosion.ogg")
        pygame.mixer.Sound.play(boom)
        sb.prep_score()
    check_high_score(stats, sb)
    if len(aliens) == 0:
        create_new_level(game_settings, screen, stats, sb, ship, aliens, 
                        bullets, aliens_bullets)

def check_ship_hit(game_settings, screen, stats, sb, ship, aliens, bullets,
aliens_bullets):
    """ Checking if the Ship was hit by an Alien Bullet """ 
    collisions = pygame.sprite.spritecollideany(ship, aliens_bullets)
    if collisions:
        ship_hit(game_settings, stats, sb, screen, ship, aliens, bullets, 
            aliens_bullets)
    
def create_new_level(game_settings, screen, stats, sb, ship, aliens, bullets, 
aliens_bullets):
    """ Creating a New Level if the Alien Amount equals 0. """
    bullets.empty()
    aliens_bullets.empty()
    game_settings.increase_difficulty()
    create_swarm(game_settings, screen, ship, aliens) 
    stats.level += 1 
    levelled = pygame.mixer.Sound("Sounds/level.wav")
    pygame.mixer.Sound.play(levelled)
    sb.prep_level()
