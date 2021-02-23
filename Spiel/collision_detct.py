import pygame
z = 0
a = 0
def check_moves(player_coords,savedlist):
    x = [5,54,103,152,201,299,348,446,544,642,691,740,789,838,887,936,985,1034,1132,1181,1230,1279,1328,1426,1475,1524,1573,1622]
    y = [6,55,104,153,202,300,349,447,545,643,692,741,790,839,888,937,986]
    
def wall_collision(walls,player):
    wall1 = pygame.Rect(walls[0])
    wall2 = pygame.Rect(walls[1])
    wall3 = pygame.Rect(walls[2])
    wall4 = pygame.Rect(walls[3])
    wall5 = pygame.Rect(walls[4])
    wall6 = pygame.Rect(walls[5])
    wall7 = pygame.Rect(walls[6])
    wall8 = pygame.Rect(walls[7])
    wall9 = pygame.Rect(walls[8])
    wall10 = pygame.Rect(walls[9])
    wall11 = pygame.Rect(walls[10])
    wall12 = pygame.Rect(walls[11])
    player_rect = pygame.Rect(player[0],player[1],44,44)
    if wall1.colliderect(player_rect) or  wall2.colliderect(player_rect) or  wall3.colliderect(player_rect) or  wall4.colliderect(player_rect) or  wall5.colliderect(player_rect) or wall6.colliderect(player_rect):
        pygame.quit()
    if wall7.colliderect(player_rect) or  wall8.colliderect(player_rect) or  wall9.colliderect(player_rect) or  wall10.colliderect(player_rect) or  wall11.colliderect(player_rect) or  wall12.colliderect(player_rect):
        pygame.quit()        
def move(screen,player_coords):
    blue = pygame.Color('blue')
    player_rect = pygame.Rect(player_coords[0],player_coords[1],44,44)
    field = pygame.Rect(player_coords[0],player_coords[1],44,44)
    if player_rect.colliderect(field):
        print('lost')
    move = pygame.draw.rect(screen,blue,field)

def drawing(screen,walls):
    blue = pygame.Color('blue')
    red = pygame.Color('red')
    purple = pygame.Color('purple')
    orange = pygame.Color('orange')
    green = pygame.Color('green')
    yellow = pygame.Color('yellow')
    wall1 = pygame.draw.rect(screen,blue,walls[0])
    wall2 = pygame.draw.rect(screen,red,walls[1])
    wall3 = pygame.draw.rect(screen,purple,walls[2])
    wall4 = pygame.draw.rect(screen,orange,walls[3])
    wall5 = pygame.draw.rect(screen,green,walls[4])
    wall6 = pygame.draw.rect(screen,yellow,walls[5])
    wall7 = pygame.draw.rect(screen,blue,walls[6])
    wall8 = pygame.draw.rect(screen,red,walls[7])
    wall9 = pygame.draw.rect(screen,purple,walls[8])
    wall10 = pygame.draw.rect(screen,orange,walls[9])
    wall11 = pygame.draw.rect(screen,green,walls[10])
    wall12 = pygame.draw.rect(screen,yellow,walls[11])

def check_reset(player_coords,coords):
    
    SavedList = [player_coords[-2],player_coords[-1]]
    
    coords.append(SavedList)
    coords.reverse()
