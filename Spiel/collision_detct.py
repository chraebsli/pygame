import pygame
z = 0
a = 0
def check_moves(player_coords,savedlist):
    x = [5,54,103,152,201,299,348,446,544,642,691,740,789,838,887,936,985,1034,1132,1181,1230,1279,1328,1426,1475,1524,1573,1622]
    y = [6,55,104,153,202,300,349,447,545,643,692,741,790,839,888,937,986]
    

def wall_collision(walls,player):
    wall_list=[]
    #wall_list=['wall1','wall2','wall3','wall4','wall5','wall6','wall7','wall8','wall9','wall10','wall11','wall12']
    c=0
    for wall in range(len(walls)):
        w=pygame.Rect(walls[c])
        wall_list.append(w)
        c+=1
    player_rect = pygame.Rect(player[0],player[1],44,44)
    for wall in wall_list:
        if wall.colliderect(player_rect):
            print('Quit...')
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
    colors=[blue,red,purple,orange,green,yellow]
    c1,c=0,0
    for wall in range(len(walls)):
        pygame.draw.rect(screen,colors[c1],walls[c])
        c+=1
        c1+=1
        if c1==5:
            c1=0


def check_reset(player_coords,coords):
    SavedList = [player_coords[-2],player_coords[-1]]
    coords.append(SavedList)
    coords.reverse()
