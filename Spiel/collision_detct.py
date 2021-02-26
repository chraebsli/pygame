import pygame


def wall_collision(walls,player):
    c=0
    player_rect = pygame.Rect(player[0],player[1],44,44)
    for wall in range(11):
        wall=pygame.Rect(walls[c])
        c+=1
        if wall.colliderect(player_rect):
            return 'titlescreen.True'


# zeigt path an
def run(screen,player) :
    blue = pygame.Color('blue')
    pygame.Rect(player[0],player[1],44,44)
    field = pygame.Rect(player[0],player[1],44,44)
    pygame.draw.rect(screen,blue,field)


# erstellt liste für alle felder (weisse quadrate)
def move(screen,player_coords,statement):
    green = pygame.Color(255, 255, 255, 128)
    pygame.Rect(player_coords[0],player_coords[1],44,44)
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


# collisiondetect für begangene felder und speichert sie
def collideplayer(player,list_coords,remo_list,statement):
    player_rect = pygame.Rect(player[0],player[1],44,44)
    pygame.Rect(player[0],player[1],44,44)
    if statement == True:
        for blocks in list_coords:
            if player_rect.colliderect(blocks):
                x = blocks
        if x in list_coords:
            if x in remo_list:
                print('lost')
                remo_list=str(remo_list)+'.True'
        return remo_list
    elif statement == False:
        for blocks in list_coords:
            if player_rect.colliderect(blocks):
                x = blocks
        if x in list_coords:
            remo_list.append(x)
            return remo_list


# zeichnet wände
def drawing(screen,walls):
    red = pygame.Color('red')
    c=0
    for e in range(11):
        pygame.draw.rect(screen,red,walls[c])
        c+=1


# playerpath 
def playerpath(remo_list,screen,player):
    blue = pygame.Color('blue')
    pygame.Rect(player[0],player[1],44,44)
    for element in remo_list:
        pygame.draw.rect(screen,blue,element)
