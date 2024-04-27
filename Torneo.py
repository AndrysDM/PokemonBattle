import random as rd
from copy import deepcopy
from tools import milog as ln

def descalificar(players):
    size = len(players)
    p = 8 * 8 * 8 * 8 * 8
    while p > size:
        p = p // 2
    print("de los que se descalificaron", size - p)
    for i in range(p, size):
        u = len(players) - 1
        print(players[u])
        players.pop()
    print('\n\n\n')

def enfrentar(player1, player2):
    return player1 if rd.randint(1,2) == 1 else player2

def torneo(players):
    size = len(players)
    li = ln(size)
    base = []
    p = 1
    for i in range(11):
        tmp = []
        if p > size:
            break
        for j in range(p):
            tmp.append({'y':0,'x':0,'yhijo':0,'win':0,'player':''})
        base.append(tmp)
        p *= 2
    
    posiciones_iniciales_y = [2*(size//4-i)-1 for i in range(size//2)]
    posiciones_iniciales_y = posiciones_iniciales_y + posiciones_iniciales_y

    for j in range(0, len(players)):
        base[len(base) - 1][j] = {'y': posiciones_iniciales_y[j],'win':0,'x': ((li-1)*2 if j < size//2 else -(li-1)*2), 'player': {'name':players[j][1], 'foto': players[j][0], 'tipo': players[j][2]}}
    
    i = len(base) - 1
    while i > 0:
        print('\n\n\nResultados de la ronda numero', li - i)
        j = 0
        while j < len(base[i]):
            base[i-1][j//2]['player'] = deepcopy(enfrentar(base[i][j]['player'],base[i][j+1]['player']))
            base[i-1][j//2]['y']=(base[i][j]['y']+base[i][j+1]['y'])//2
            base[i-1][j//2]['x']=base[i][j]['x'] - (2 if base[i][j]['x'] > 0 else -2)  

            if( base[i-1][j//2]['player'] == base[i][j]['player']):
                base[i][j]['win'] = 1
            else:
                base[i][j+1]['win'] = 1

            base[i][j]['yhijo']=base[i-1][j//2]['y']
            base[i][j+1]['yhijo']=base[i-1][j//2]['y']
            
            j += 2
        i -= 1
    return base
