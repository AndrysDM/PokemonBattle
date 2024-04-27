import os
from PlotRonda import plot_ronda
from copy import deepcopy
ruta=os.getcwd()
fotobola=(os.path.join(ruta,'assets'))
fotobola=(os.path.join(fotobola,'poke-ball.png'))

#basee=[[{'y': 0, 'x': 0, 'yhijo': 0, 'win': 0, 'player': {'name': 1583, 'foto': 'C:\\Users\\Thinkpad\\Desktop\\Python\\Clases de python\\Proyecto Ping Pong\\assets\\Pokemon Grande\\25.jpg'}}], [{'y': 0, 'x': 2, 'yhijo': 0, 'win': 0, 'player': {'name': 2544, 'foto': 'C:\\Users\\Thinkpad\\Desktop\\Python\\Clases de python\\Proyecto Ping Pong\\assets\\Pokemon Grande\\25.jpg'}}, {'y': 0, 'x': -2, 'yhijo': 0, 'win': 1, 'player': {'name': 1583, 'foto': 'C:\\Users\\Thinkpad\\Desktop\\Python\\Clases de python\\Proyecto Ping Pong\\assets\\Pokemon Grande\\25.jpg'}}], [{'y': 1, 'win': 1, 'x': 4, 'player': {'name': 2544, 'foto': 'C:\\Users\\Thinkpad\\Desktop\\Python\\Clases de python\\Proyecto Ping Pong\\assets\\Pokemon Grande\\25.jpg'}, 'yhijo': 0}, {'y': -1, 'win': 0, 'x': 4, 'player': {'name': 5555, 'foto': 'C:\\Users\\Thinkpad\\Desktop\\Python\\Clases de python\\Proyecto Ping Pong\\assets\\Pokemon Grande\\25.jpg'}, 'yhijo': 0}, {'y': 1, 'win': 1, 'x': -4, 'player': {'name': 1583, 'foto': 'C:\\Users\\Thinkpad\\Desktop\\Python\\Clases de python\\Proyecto Ping Pong\\assets\\Pokemon Grande\\25.jpg'}, 'yhijo': 0}, {'y': -1, 'win': 0, 'x': -4, 'player': {'name': 8913, 'foto': 'C:\\Users\\Thinkpad\\Desktop\\Python\\Clases de python\\Proyecto Ping Pong\\assets\\Pokemon Grande\\25.jpg'}, 'yhijo': 0}]]
def GenerarPlotsRonda(base):
    rondas = len(base)
    for i in range(rondas+1):
        print('ronda ',i)
        tmp = deepcopy(base)
        for j in range(0,len(tmp)-i):
            for k in tmp[j]:
                k['player']['foto'] = fotobola
                k['player']['name'] = ''
                k['win']=0
        plot_ronda(tmp,i)
        