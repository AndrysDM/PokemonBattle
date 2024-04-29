from tools import asignar_colores_a_tipos
import numpy as np
from tools import hex_to_rgb
import matplotlib.pyplot as plt
from PIL import Image
mapa_de_tipo_color = asignar_colores_a_tipos()
def matriz_color(tipostr):
    tipos=tipostr.split('/')
    
    colores = [mapa_de_tipo_color[i] if i!='none' else '#000000' for i in tipos]
    
    color_start = hex_to_rgb(colores[0])
    color_end = hex_to_rgb(colores[-1])

    color_start = np.array([i for i in color_start] + [1])
    color_end = np.array([i for i in color_end] + [1])

    tam = 1000

    Z = [[i+j+0.0 for j in range(tam)]for i in range(tam)]
    Z = np.array(Z)
    Z /= np.max(Z)

    color = np.zeros((tam, tam, 4))
    for i in range(tam):
        for j in range(tam):
            t = Z[i, j]  # Valor en el punto (i, j)
            color[i, j] = (1 - t) * color_start + t * color_end
            if((i-tam/2)**2 + (j-tam/2)**2 < (tam/2)**2):
                color[i, j] = (1 - t) * color_start + t * color_end
            else:
                #print('dldadsa')
                color[i, j] = np.array([0,0,0,0])
            #color[i, j] = (1 - t) * color_start + t * color_end
    return color


def ponerfondo(player):
    plt.figure(figsize=(10, 10))
    foto = player[0]
    img = Image.open(foto)
    color = matriz_color(player[2])
    x=0
    y=0
    plt.imshow(img, extent=(x - 0.5, x + 0.5, y - 0.5, y + 0.5), aspect='auto', zorder = 3)
    plt.imshow(color, extent=(x - 0.5, x + 0.5, y - 0.5, y + 0.5), aspect='auto', zorder = 1)
            
    plt.tight_layout()
    plt.axis('off')
    tmp = player[0]
    tmp=tmp.replace('assets\\Pokemon Grande','fotos_con_fondo')
    plt.savefig(tmp)
import os
def generar_fotos_fondo(players):
    for player in players:
        tmp = player[0]
        tmp=tmp.replace('assets\\Pokemon Grande','fotos_con_fondo')
        print(tmp)
        if not os.path.exists(tmp):
            ponerfondo(player)
