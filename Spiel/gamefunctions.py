import pygame,datetime,json,collision_detct,sqlite3

randskin = 1
randcoin = 1


# display walls
def wall_blit(screen,walls,wall_coords_xy):
    c=1
    for wall in walls:
        screen.blit(wall,wall_coords_xy[c])
        c+=1


# display background
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


# animated skin for end
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


# animated skin for coin
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


# write score
def scores(points,name,played_time,path):
    global str_time
    # gives date and time dd.mm.yyyy hh:mm:ss
    actual=datetime.datetime.now()
    date=actual.strftime('%d.%m')
    time=actual.strftime('%H:%M')
    now=date+' '+time
    
    conn = sqlite3.connect(path + '/coinchaser.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO leaderboard (crdate, playername, points, playedTime) VALUES (?,?,?,?)", (now, name, points, played_time))
    conn.commit()
    conn.close()

    
#zeigt die aktuelle Punkteanzahl an, falls der Spieler in game 'Q' drückt   
def show_points(points,remo_list,screen,coins_rect,t3):
        global str_time
        time = datetime.datetime.now() - t3
        color = pygame.Color('white')
        black = pygame.Color('black')
        base_font = pygame.font.SysFont(None, 160)
        points = collision_detct.point_counter(points,remo_list,coins_rect)
        final_punkte = points + int(len(remo_list))
        text_surface = base_font.render(f'Points: {final_punkte+1}',False,black)
        str_time = str(time)
        timelabel = base_font.render(f'Time: {str_time[2:7]}', True, (0,0,0))
        pygame.draw.rect(screen, color,(0,0,2000,100))
        screen.blit(text_surface,(150, 5))
        screen.blit(timelabel,(900, 5))


# calculate points: rechnet die Finalpunktzahl aus, falls der Spieler das Spiel erfolgreich beendet
def calculate_points(points,remo_list,coins_rect):
        points = collision_detct.point_counter(points,remo_list,coins_rect)
        final_punkte = points + int(len(remo_list))
        return final_punkte-1


def return_endtime(t3): #gibt, falls der Spieler das Spiel beendet, seine Spielzeit zurück
        global str_time
        time = datetime.datetime.now() - t3
        str_time = str(time)
        str_time_min = str_time[3:9]
        return str_time_min


# starts a timer
def start_timer():
    t1 = datetime.datetime.now()
    return t1


# ends a timer
def end_timer(t1,msg):
    t2 = datetime.datetime.now()
    print ('\nTime collabsed' + msg + ': ' + str(t2 - t1)[5:] + ' seconds\n')


#Schaut beim Login Screen, ob der Account schon existriert
def check_account_exsistance(playername,password,path):
    verbindung = sqlite3.connect(path + '/coinchaser.db')
    zeiger = verbindung.cursor()

    sql = 'CREATE TABLE IF NOT EXISTS daten(benutzername TEXT,passwort TEXT)'
    zeiger.execute(sql)

    zeiger.execute("SELECT benutzername,passwort FROM daten")
    inhalt = zeiger.fetchall()
    combine = (playername,password)
    if combine in inhalt:
        x = 'this account exists'
    else:
        x = 'Try Again'
    verbindung.close()
    return x


#Account in Datenbank registrieren
def register_account(playername,password,path,statement):
    verbindung = sqlite3.connect(path + '/coinchaser.db')
    zeiger = verbindung.cursor()
    if statement == True: # Dieser Block überprüft, ob es den Benutzernamen schon gibt.
        zeiger.execute("SELECT benutzername FROM daten")
        inhalt = zeiger.fetchall()
        change_format = (playername,)
        if change_format in inhalt:
            return 'benutzername vergeben' 
        else:
             return 'ok'
    if statement == False: #Dieser Block schreibt die Daten in die Datenbank
        combine = (playername,password,0)
        zeiger.execute("INSERT INTO daten VALUES (?,?,?)",combine)
        verbindung.commit()


#Zeigt die Summe von Punkten an, welche mit dem Account gewonnen wurde 
def show_account_points(playername,path,password):
    verbindung = sqlite3.connect(path + '/coinchaser.db')
    zeiger = verbindung.cursor()
    
    zeiger.execute("SELECT points FROM daten WHERE benutzername = ? AND passwort = ?",(playername,password))
    inhalt = zeiger.fetchall()
    return f'CC-POINTS: {str(inhalt[0][0])}'


#Aktualisiert nach einer erfolgreichen Runde die Account Punkte
def renew_acc_points(playername,path,password,game_points):
    verbindung = sqlite3.connect(path + '/coinchaser.db')
    zeiger = verbindung.cursor()
    
    zeiger.execute("SELECT points FROM daten WHERE benutzername = ? AND passwort = ?",(playername,password))
    inhalt = zeiger.fetchall()
    int_points = int(inhalt[0][0])
    int_points += game_points
    zeiger.execute("UPDATE daten SET points = ? WHERE benutzername = ? AND passwort = ?",(int_points,playername,password))
    verbindung.commit()
