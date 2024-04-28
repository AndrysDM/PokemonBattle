import os
from PlotRonda import plot_ronda
from copy import deepcopy
ruta=os.getcwd()
carpeta_destino=(os.path.join(ruta,'rondas_del_torneo'))
fotobola=(os.path.join(ruta,'assets'))
fotobola=(os.path.join(fotobola,'poke-ball.png'))
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)
def GenerarPlotsRonda(base):
    rondas = len(base)
    for i in range(rondas+1):
        print('ronda ',i)
        tmp = deepcopy(base)
        for j in range(0,rondas-i):
            for k in tmp[j]:
                k['player']['foto'] = fotobola
                k['player']['name'] = ''
                k['win']=0
                k['player']['tipo']='none'
        if(rondas-i >= 0  and rondas - i < rondas):
            for k in tmp[rondas-i]:
                k['win'] = 0
        plot_ronda(tmp,i)
        