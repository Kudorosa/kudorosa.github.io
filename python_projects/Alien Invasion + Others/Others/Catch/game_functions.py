import pygame 
import sys
from balls import Ball
from bullets import Bullet
from time import sleep

def ball_dropped(game_settings, stat, screen, human, balls, bullets):
    """ If the Ball is dropped, Substract from the Number of Tries """ 
    #Substract One Try from the Number of Tries.
    stat.tries_left -= 1 
    if stat.tries_left > 0: 
        
        balls.empty()
        bullets.empty()
        
        create_barrage(game_settings, screen, human, balls)
        
        sleep(0.3)
        
    else:
        stat.game_ongoing = False
        
def check_ball_dropped(game_settings, stat, screen, human, balls, bullets):
    """ Checking if the Ball was dropped """ 
    screen_rect = screen.get_rect()
    for ball in balls.sprites():
        if ball.rect.bottom >= screen_rect.bottom:
            ball_dropped(game_settings, stat, screen, human, balls, bullets)
            break
            
    


def get_number_rows(game_settings, human_height, ball_height):
    """ Number of Rows for the Aliens """ 
    current_space_y = (game_settings.screen_height - 
                    (3 * ball_height) - human_height)   
    number_rows = int(current_space_y / (4 * ball_height))
    return number_rows
    
def get_number_balls_x(game_settings, ball_width): 
    """ Getting the Number of Aliens """ 
    current_space_x = game_settings.screen_width - 8 * ball_width
    number_balls_x = int(current_space_x / (8 * ball_width)) 
    return number_balls_x

def create_balls(game_settings, screen, balls, ball_count, row_number): 
    """ Creating an Alien """ 
    ball = Ball(screen, game_settings)
    ball_width = ball.rect.width
    ball.x = ball_width + 1 * ball_width * ball_count
    ball.rect.x = ball.x
    ball.rect.y = ball.rect.height + 1 * ball.rect.height * row_number
    balls.add(ball) 

def create_barrage(game_settings, screen, human, balls):
    """ Creating a Swarm of Aliens """ 
    #Spacing between Aliens is equal to one ball Width.
    ball = Ball(screen, game_settings) 
    number_balls_x = get_number_balls_x(game_settings, ball.rect.width)
    number_rows = get_number_rows(game_settings, human.rect.height, 
                                                        ball.rect.height)
    
    #Creating the First Row of Balls. 
    for row_number in range(number_rows):
        for ball_count in range(number_balls_x): 
            create_balls(game_settings, screen, balls, ball_count, 
                                                                    row_number) 

def check_ball_bounds(game_settings, screen, human, balls):
    """ Checking the Swarm's Edges """
    for ball in balls.sprites():
        if ball.check_bounds(): 
            break
    
def update_balls(game_settings, stat, screen, human, balls, bullets):
    """ Updating the Aliens so they can move
    and checking if they are at the Edge of the Screen """ 
    check_ball_bounds(game_settings, screen, human, balls) 
    balls.update() 
    check_ball_dropped(game_settings, stat, screen, human, balls, bullets)
        

def keyup_event(event, game_settings, screen, human, bullets):
    """ Checking for Keyup Events """ 
    #Left and Right Controls Release.
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        human.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        human.moving_left = False

def keydown_event(event, game_settings, screen, human, bullets):
    """ Checking for Keydown Events. """ 
    #Left and Right Controls.
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        human.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        human.moving_left = True
        
    #Shooting.
    elif event.key == pygame.K_SPACE:
        shoot(game_settings, screen, human, bullets)      
    
    #Quit
    elif event.key == pygame.K_q: 
        sys.exit()
        
def mouse_event(event, game_settings, screen, human, bullets):
    """ Mouse Controls """ 
    #Shooting Controls. 
    if event.button == 1:
        shoot(game_settings, screen, human, bullets)
        
def shoot(game_settings, screen, human, bullets):
    """ Shoot Now! """ 
    if len(bullets) < game_settings.capacity:
        new_bullet = Bullet(game_settings, screen, human) 
        bullets.add(new_bullet) 

    
        
def check_events(game_settings, screen, human, bullets):
    """ Allows for the Checking of Player Inputs """ 
    for event in pygame.event.get():
        if event == "QUIT":
            sys.exit() 
            
            """ Keyboard & Mouse Events """
        elif event.type == pygame.KEYDOWN:
            keydown_event(event, game_settings, screen, human, bullets)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_event(event, game_settings, screen, human, bullets)
            
        elif event.type == pygame.KEYUP:
            keyup_event(event, game_settings, screen, human, bullets)
            
        
def calibrate_screen(game_settings, screen, human, balls, bullets): 
    """ """ 
    """ Allowing for the Screen to be constantly updated """ 
    pygame.display.flip() 
    screen.fill(game_settings.bg_colour)
    balls.draw(screen)
    human.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
   
def update_bullets(game_settings, screen, human, balls, bullets):
    """ """ 
    bullets.update() 
    
    for bullet in bullets.copy(): 
        if bullet.rect.bottom <= 0: 
            bullets.remove(bullet)
    check_ball_hit(game_settings, screen, human, balls, bullets)
       
       
def check_ball_hit(game_settings, screen, human, balls, bullets):
    """ Check to see if any Alien(s) were hit by Bullet(s) """ 
    #Checking for any Bullets that hit an Alien.
    ball = Ball(screen, game_settings)
    if len(balls) == 0 or pygame.sprite.spritecollideany(human, balls):
        balls.empty()
        create_barrage(game_settings, screen, human, balls) 
