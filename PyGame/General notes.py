import pygame
from random import randint

# Initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Wayless')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 45)

# Variable init
game_active = False
start_time = 0
player_gravity = 0
it = True

shrimpspeed = 0

# Timer & Userevent
obstacle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer, 1500)

def display_score():
    timeingame = pygame.time.get_ticks() - start_time
    scoreis = font.render(str(int(timeingame / 1000)), False, (64,64,64))
    scoreisrectangle = scoreis.get_rect(topleft = (10, 10))
    screen.blit(scoreis, scoreisrectangle)

# Surfaces and rectangles
textsurface = font.render('press space', False, (64,64,64))
textrectangle = textsurface.get_rect(center = (400, 100))

colorsurface = pygame.Surface((100,200))
colorsurface.fill('Green')

backgroundsurface = pygame.image.load('./images/background.png').convert()
backgroundrectangle = backgroundsurface.get_rect(topleft = (0,0))

groundsurface = pygame.image.load('./images/ground.png').convert()

# obstacles
obstaclerectangles = []

shrimpsurface = pygame.image.load('./images/shrimp.png').convert_alpha()
shrimprectangle = shrimpsurface.get_rect(bottomright = (800, 500))
flysurface = pygame.image.load('./images/fly.png').convert_alpha()
flyrectangle = flysurface.get_rect(bottomright = (800, 400))

def obstacle_movement(olist):
    if len(olist) >= 1:
        for rect in olist:
            rect.x -= 5
            if rect.bottom >= 500:
                screen.blit(shrimpsurface, rect)
            else:
                screen.blit(flysurface, rect)
        olist = [obst for obst in olist if obst.x > -100]
        return olist
    else:
        print('oh no')
        return []
    
def collissions(player, obstacles):
    if obstacles:
        for each in obstacles:
            if player.colliderect(each):
                return True
    return False
        
playersurface = pygame.image.load('./images/player.png').convert_alpha()
playersurfacescaled = pygame.transform.rotozoom(playersurface, 0, 3)   #rotozoom (surface, rotation(degrees), scale (x100%))
playerrectangle = playersurface.get_rect(bottomleft = (50, 500))
playerrectanglescaled = playersurfacescaled.get_rect(center = (400,300))

# Run Loop
while it is True:
    if game_active is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                it = False
            if event.type == obstacle_timer:
                print('adding')
                print(len(obstaclerectangles))
                if randint(0, 2) >= 1:
                    obstaclerectangles.append((shrimpsurface.get_rect(bottomright = (randint(900, 1100), 500))))
                else:
                    obstaclerectangles.append((flysurface.get_rect(bottomright = (randint(900, 1100), 380))))
            if event.type == pygame.MOUSEMOTION:
                print(event.pos)
                if playerrectangle.collidepoint(event.pos):
                    print('on top of player!')
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('click!')
                if playerrectangle.collidepoint((event.pos)):
                    if playerrectangle.bottom >= 499:
                        player_gravity = -25
            if event.type == pygame.MOUSEBUTTONUP:
                print('unclick!')    
            
            if event.type == pygame.KEYDOWN:
                print('keydown!')
                if event.key == pygame.K_SPACE:
                    print ('keydown on space specifically')
                    if playerrectangle.bottom >= 499:
                        player_gravity = -20
            if event.type == pygame.KEYUP:
                print('Keyup!')   
                 
        screen.blit(backgroundsurface, backgroundrectangle)        
        screen.blit(groundsurface, (0, 500))
     
        # Obstacles
        obstaclerectangles = obstacle_movement(obstaclerectangles)
            
        player_gravity += 1
        playerrectangle.y += player_gravity
        if playerrectangle.bottom >= 500:
            playerrectangle.bottom = 500
        screen.blit(playersurface, playerrectangle)

        pygame.draw.line(screen, 'Orange', playerrectangle.topright, pygame.mouse.get_pos(), 6)
        pygame.draw.ellipse(screen,'Brown', pygame.Rect(50,200,200,100))
    
        pygame.draw.rect(screen, '#c0e8ec', textrectangle, 16)
        pygame.draw.rect(screen, '#c0e8ec', textrectangle)
        screen.blit(textsurface, textrectangle)
        
        if playerrectangle.colliderect(shrimprectangle):
            print('shrimpcollision')
        if collissions(playerrectangle, obstaclerectangles):
            game_active = False
    
        keys = pygame.key.get_pressed() #find keys online. 
    
        for each in pygame.key.get_pressed():
            if each != False:
                print(each)
    
        if keys[pygame.K_SPACE]:
            print('space is pressed')
        
        mouse_pos = pygame.mouse.get_pos()
        if playerrectangle.collidepoint((mouse_pos)):
            print('mousecollission')
            print(pygame.mouse.get_pressed()) #returns for 3 buttons on mouse (bool, bool, bool))
            
    # Inactive game   
    else:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print('keydown!')
                if event.key == pygame.K_SPACE:
                    shrimpspeed = 0
                    game_active = True
                    start_time = pygame.time.get_ticks()
            if event.type == pygame.QUIT:
                it = False
        
        #resetting          
        obstaclerectangles.clear()
        playerrectangle.bottomleft = (50, 500)
        player_gravity = 0
        
        screen.blit(backgroundsurface, backgroundrectangle)
        screen.blit(textsurface, textrectangle)
        screen.blit(playersurfacescaled, playerrectanglescaled)
    
    display_score()
        
    pygame.display.update()
    
    clock.tick(60)
        
   
'''
 spritecollide group vs group:
 pygame.sprite.spritecollide(sprite, group, bool)
 
 sound
   sound = pygame.mixer.Sound('path to fil.mp3')   
   sound.set_volume(0 = (nothing) to 1 = (full))
   sound.play
   sound.play(loops = -1 (forever) or any int)
 '''       
    