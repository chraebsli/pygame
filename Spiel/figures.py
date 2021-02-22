import pygame, random

# randomskin für das Ziel
def rand_endskin(path1,end1):
    randskin = random.randint(1,6)
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
    
    return end1
