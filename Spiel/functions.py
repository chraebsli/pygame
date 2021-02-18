import itertools
def del_duplicates(player_coords):
    x=[]
    x=player_coords
    x.sort()
    player_coords = list(x for x,_ in itertools.groupby(x))
    return player_coords
