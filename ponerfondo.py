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

    Z = [[i+0.0 for j in range(100)]for i in range(100)]
    Z = np.array(Z)
    Z /= 100.0

    color = np.zeros((100, 100, 4))
    for i in range(Z.shape[0]):
        for j in range(Z.shape[1]):
            t = Z[i, j]  # Valor en el punto (i, j)
            color[i, j] = (1 - t) * color_start + t * color_end
            if((i-50)**2 + (j-50)**2 < 50**2):
                color[i, j] = (1 - t) * color_start + t * color_end
            else:
                color[i, j] = np.array([0,0,0,0])
            #color[i, j] = (1 - t) * color_start + t * color_end
    return color


def ponerfondo(player, sub_carp):
    plt.figure(figsize=(10, 10))
    foto = player['foto']
    img = Image.open(foto)
    color = matriz_color(player['tipo'])
    x=0
    y=0
    plt.imshow(img, extent=(x - 0.5, x + 0.5, y - 0.5, y + 0.5), aspect='auto', zorder = 3)
    plt.imshow(color, extent=(x - 0.5, x + 0.5, y - 0.5, y + 0.5), aspect='auto', zorder = 1)
            

    # Ajustar los límites del gráfico para que se ajusten a los puntos
    # limmax = 0.5
    # plt.xlim(-limmax, limmax)
    # plt.ylim(-limmax, limmax)

    # Guardar el gráfico en el archivo especificado
    plt.tight_layout()
    plt.axis('off')
    plt.savefig(f'./fotos_con_fondo/{sub_carp}-{foto[-5:]}')


probando = {'name': 'Chansey', 'foto': 'C:\\Users\\Thinkpad\\Desktop\\Python\\Clases de python\\PokemonBattle\\assets\\Pokemon Grande\\113.png', 'tipo': 'Normal/Dragón'}
ponerfondo(probando,"descalificados")