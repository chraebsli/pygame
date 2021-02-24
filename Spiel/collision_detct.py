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
<<<<<<< HEAD
    if wall1.colliderect(player_rect) or  wall2.colliderect(player_rect) or  wall3.colliderect(player_rect) or  wall4.colliderect(player_rect) or  wall5.colliderect(player_rect) or wall6.colliderect(player_rect):
        pygame.quit()
    if wall7.colliderect(player_rect) or  wall8.colliderect(player_rect) or  wall9.colliderect(player_rect) or  wall10.colliderect(player_rect) or  wall11.colliderect(player_rect) or  wall12.colliderect(player_rect):
        pygame.quit()   
def run(screen,player) :
=======
    for wall in wall_list:
        if wall.colliderect(player_rect):
            print('Quit...')
            pygame.quit()


def move(screen,player_coords):
>>>>>>> c8928eb768c39f0ea7739b01ae948897aceb8c7b
    blue = pygame.Color('blue')
    player_rect = pygame.Rect(player[0],player[1],44,44)
    field = pygame.Rect(player[0],player[1],44,44)
    moves = pygame.draw.rect(screen,blue,field)
def move(screen,player_coords,statement):
    blue = pygame.Color('blue')
    green = pygame.Color(255, 255, 255, 128)
    do = False
    player_rect = pygame.Rect(player_coords[0],player_coords[1],44,44)
    field = pygame.Rect(player_coords[0],player_coords[1],44,44)
<<<<<<< HEAD
    
    
    x = 0
    y = 0
    if statement == False:
        list_coords = []
        while x != 34 and y != 21:
            buttons = pygame.Rect(0+((50-1)*x+7),0+((50-1)*y+7),44,44)
            places = pygame.draw.rect(screen,green,buttons)
            list_coords.append(places)
            x += 1
            if x == 34:
                y+=1
                x=0
        return list_coords
    if statement == True:   
        while x != 34 and y != 21:
            buttons = pygame.Rect(0+((50-1)*x+7),0+((50-1)*y+7),44,44)
            places = pygame.draw.rect(screen,green,buttons)
            x += 1
            if x == 34:
                y+=1
                x=0
def collideplayer(player,list_coords,remo_list):
    blue = pygame.Color('blue')
    player_rect = pygame.Rect(player[0],player[1],44,44)
    field = pygame.Rect(player[0],player[1],44,44)
    for blocks in list_coords:
        if player_rect.colliderect(blocks):
            x = blocks
    if x in list_coords:
        if x in remo_list:
            print('lost')
            pygame.quit()
        else:
            remo_list.append(x)
            print('remo updated')
        return remo_list
=======
    if player_rect.colliderect(field):
        print('lost')
    move = pygame.draw.rect(screen,blue,field)


>>>>>>> c8928eb768c39f0ea7739b01ae948897aceb8c7b
def drawing(screen,walls):
    blue = pygame.Color('blue')
    red = pygame.Color('red')
    purple = pygame.Color('purple')
    orange = pygame.Color('orange')
    green = pygame.Color('green')
    yellow = pygame.Color('yellow')
<<<<<<< HEAD
    wall1 = pygame.draw.rect(screen,red,walls[0])
    wall2 = pygame.draw.rect(screen,red,walls[1])
    wall3 = pygame.draw.rect(screen,red,walls[2])
    wall4 = pygame.draw.rect(screen,red,walls[3])
    wall5 = pygame.draw.rect(screen,red,walls[4])
    wall6 = pygame.draw.rect(screen,red,walls[5])
    wall7 = pygame.draw.rect(screen,red,walls[6])
    wall8 = pygame.draw.rect(screen,red,walls[7])
    wall9 = pygame.draw.rect(screen,red,walls[8])
    wall10 = pygame.draw.rect(screen,red,walls[9])
    wall11 = pygame.draw.rect(screen,red,walls[10])
    wall12 = pygame.draw.rect(screen,red,walls[11])
=======
    colors=[blue,red,purple,orange,green,yellow]
    c1,c=0,0
    for wall in range(len(walls)):
        pygame.draw.rect(screen,colors[c1],walls[c])
        c+=1
        c1+=1
        if c1==5:
            c1=0

>>>>>>> c8928eb768c39f0ea7739b01ae948897aceb8c7b

def playerpath(remo_list,screen,player):
    blue = pygame.Color('blue')
    player_rect = pygame.Rect(player[0],player[1],44,44)
    for element in remo_list:
        path5 = pygame.draw.rect(screen,blue,element)
def check_reset(player_coords,coords):
    SavedList = [player_coords[-2],player_coords[-1]]
    coords.append(SavedList)
    coords.reverse()
