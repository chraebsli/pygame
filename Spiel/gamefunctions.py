import git
import pygame,datetime,json,collision_detct
from git import Repo

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


def scores(points,name,path):
    # gives date and time dd.mm.yyyy hh:mm:ss
    actual=datetime.datetime.now()
    date=actual.strftime('%d.%m')
    time=actual.strftime('%H:%M')
    now=date+' '+time

    # get data in json 
    with open(path+'scores/web/scores.json') as file:
        data = json.load(file)
    data['scores'].append({'time':now,'name':name,'points':points})
    with open(path+'scores/web/scores.json','w') as file:
        json.dump(data,file,indent=4)

    # sortiert die liste nach höchstpunktzahl
    with open(path+'scores/web/scores.json') as file:
        data_score = json.load(file)
        data_score['scores'] = list(sorted(data_score['scores'],key=lambda p: p['points'],reverse=True))
    with open(path+'scores/web/scores.json','w') as file:
        json.dump(data_score,file,indent=4)
    
    
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

def start_timer():
    t1 = datetime.datetime.now()
    return t1


def end_timer(t1,msg):
    t2 = datetime.datetime.now()
    print ('\nTime collabsed' + msg + ': ' + str(t2 - t1)[5:] + ' seconds\n')


def clone_repo(path,remote):
    global repo
    try:
        repo = Repo.clone_from(remote, path)
        print('Cloned repo for scores')
    except:
        repo = git.Repo(path+'/.git')
        return False


def pull_repo(prepo):
    global repo
    try:
        repo.pull()
        print('pulled1')
    except:
        try:
            repo = git.Repo(prepo+'/.git')
            repo.pull()
            print('pulled2')
        except:
            print('Error while pulling repo')


def push_repo(remote,prepo):
    global repo
    repo.git.add(prepo+"/web/scores.json")
    repo.index.commit("Update JSON for Leaderboard")
    repo.remotes.origin.push(refspec='master:master')
    print('Pushed Succesful')

