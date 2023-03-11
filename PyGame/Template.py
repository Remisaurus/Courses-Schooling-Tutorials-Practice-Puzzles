import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Wayless')

clock = pygame.time.Clock()
font = pygame.font.Font(None, 45)
player_gravity = 0
it = True
game_active = False

textsurface = font.render('press space', False, (64,64,64))
textrectangle = textsurface.get_rect(center = (400, 100))

backgroundsurface = pygame.image.load('./images/background.png').convert()
backgroundrectangle = backgroundsurface.get_rect(topleft = (0,0))

groundsurface = pygame.image.load('./images/ground.png').convert()

shrimpsurface = pygame.image.load('./images/shrimp.png').convert_alpha()
shrimprectangle = shrimpsurface.get_rect(bottomright = (800, 500))

playersurface = pygame.image.load('./images/player.png').convert_alpha()
playersurfacescaled = pygame.transform.rotozoom(playersurface, 0, 3) 
playerrectangle = playersurface.get_rect(bottomleft = (0, 500))
playerrectanglescaled = playersurfacescaled.get_rect(center = (400,300))

while it is True:
    if game_active is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                it = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playerrectangle.collidepoint((event.pos)):
                    if playerrectangle.bottom >= 499:
                        player_gravity = -15
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if playerrectangle.bottom >= 499:
                        player_gravity = -15
    
        shrimprectangle.x -= 3
        if shrimprectangle.right <= 0:
            shrimprectangle.left += 800
    
        screen.blit(backgroundsurface, backgroundrectangle)        
        screen.blit(groundsurface, (0, 500))
        screen.blit(shrimpsurface, shrimprectangle)
    
        player_gravity += 1
        playerrectangle.y += player_gravity
        if playerrectangle.bottom >= 500:
            playerrectangle.bottom = 500
        screen.blit(playersurface, playerrectangle)
              
    else:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
            if event.type == pygame.QUIT:
                it = False
                    
        screen.blit(backgroundsurface, backgroundrectangle)
        screen.blit(textsurface, textrectangle)
        screen.blit(playersurfacescaled, playerrectanglescaled)
    
        
    pygame.display.update()
    
    clock.tick(60)
    