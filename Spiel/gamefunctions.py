import pygame,ast,datetime,json,collision_detct

# Funktion für das setzen der Wände
def wall_blit(screen,walls,wall_coords_xy):
    c=1
    for wall in walls:
        screen.blit(wall,wall_coords_xy[c])
        c+=1

# Anzeigen von den Feldabgrenzungen
def background(screen,path):
    x,y = 1,1
    senkrechte = pygame.image.load(path + "images/gamescreen/senkrechte.png")
    gerade = pygame.image.load(path + "images/gamescreen/gerade.png")

    for s in range(1,36):
        screen.blit(senkrechte,(x,1))
        x+=49
    for h in range(1,23):
        screen.blit(gerade,(1,y))
        y+=49

# randomskin für das Ziel
randskin = 1
randcoin = 1
def random_endskin(path1,end1):
    global randskin
    if randskin == 1:
        end1 = pygame.image.load(path1 + "images/gamescreen/endskins/green.png")
    elif randskin == 2:
        end1 = pygame.image.load(path1 + "images/gamescreen/endskins/lightblue.png")
    elif randskin == 3:
        end1 = pygame.image.load(path1 + "images/gamescreen/endskins/orange.png")
    elif randskin == 4:
        end1 = pygame.image.load(path1 + "images/gamescreen/endskins/red.png")
    elif randskin == 5:
        end1 = pygame.image.load(path1 + "images/gamescreen/endskins/violet.png")
    elif randskin == 6:
        end1 = pygame.image.load(path1 + "images/gamescreen/endskins/yellow.png")
    randskin+=1
    if randskin==7:
        randskin=1
    return end1

# farbenwechselndes Ende
def random_coinskin(path1,coin1):
    global randcoin
    if randcoin == 1:
        coin1 = pygame.image.load(path1 + "images/gamescreen/coinsskins/green.png")
    elif randcoin == 2:
        coin1 = pygame.image.load(path1 + "images/gamescreen/coinsskins/lightblue.png")
    elif randcoin == 3:
        coin1 = pygame.image.load(path1 + "images/gamescreen/coinsskins/orange.png")
    elif randcoin == 4:
        coin1 = pygame.image.load(path1 + "images/gamescreen/coinsskins/red.png")
    elif randcoin == 5:
        coin1 = pygame.image.load(path1 + "images/gamescreen/coinsskins/violet.png")
    elif randcoin == 6:
        coin1 = pygame.image.load(path1 + "images/gamescreen/coinsskins/yellow.png")
    randcoin+=1
    if randcoin==7:
        randcoin=1
    return coin1


def scores(counter_felder,name,path):
    # old script
    '''
    score_file_lst=[]
    counter_coins=5
    
    with open('scores.txt','r+') as scores:
        score_file = scores.read()
        score_file_lst = list(ast.literal_eval(score_file))
        print(score_file_lst)     
        score_file_lst.append(counter_felder)
    open('scores.txt','r+').close
    
    with open('scores.txt','r+') as scores:
        scores.write(str(tuple(score_file_lst)))
        print('scores:',score_file_lst)

    actual=datetime.datetime.now()
    date=actual.strftime('%d.%m.%Y')
    time=actual.strftime('%H:%M:%S')
    now=date+' '+time

    json_data={'id':1,'data':[now,name,counter_felder,counter_coins]}
    with open('scores.json', 'r+') as scores:
        json.dump(json_data, scores, ensure_ascii=False, indent=4)
    '''
    # placeholder
    names=['name1','name2','name3','name2']
    counter_felder,counter_coins=[43,32,12,12],[3,6,6,3]
    dates = ['01.03.2021 13:05:59','01.03.2021 13:46:04','01.03.2021 14:05:59','01.03.2021 13:30:04']

    # gives date and time dd.mm.yyyy hh:mm:ss
    actual=datetime.datetime.now()
    date=actual.strftime('%d.%m.%Y')
    time=actual.strftime('%H:%M:%S')
    now=date+' '+time

    # get data in json 
    with open('scores.json', 'r+') as scores:
            result = {'items':[{'time':i[0],'name':i[1], 'felder':i[2], 'coins':i[3]} for i in zip(dates,names,counter_felder,counter_coins)]}
            json.dump(result, scores, indent=4)

    
def show_points(points,remo_list,screen,coins_rect):
        color = pygame.Color('white')
        black = pygame.Color('black')
        base_font = pygame.font.SysFont(None, 160)
        points = collision_detct.point_counter(points,remo_list,coins_rect)
        final_punkte = points + int(len(remo_list))
        text_surface = base_font.render(f'Punkte: {final_punkte+1}',False,black)
        pygame.draw.rect(screen, color,(0,0,2000,100))
        screen.blit(text_surface,(500, 5))


def calculate_points(points,remo_list,coins_rect):
        points = collision_detct.point_counter(points,remo_list,coins_rect)
        final_punkte = points + int(len(remo_list))
        return final_punkte-1
