import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from tools import asignar_colores_a_tipos
import numpy as np

mapa_de_tipo_color = asignar_colores_a_tipos()

ruta=os.getcwd()
fotourl=(os.path.join(ruta,'assets'))
save_folder=(os.path.join(ruta,'rondas_del_torneo'))

def hex_to_rgb(hex_string):
    # Eliminar el símbolo '#' del string
    hex_string = hex_string.lstrip('#')
    
    # Extraer los componentes de rojo, verde y azul del string
    red = int(hex_string[0:2], 16)
    green = int(hex_string[2:4], 16)
    blue = int(hex_string[4:6], 16)

    return np.array([red, green, blue])/256

def matriz_color(tipostr):
    tipos=tipostr.split('/')
    #print(tipos)
    colores = [mapa_de_tipo_color[i] if i!='none' else '#000000' for i in tipos]
    #print(colores)
    color_start = hex_to_rgb(colores[0])
    color_end = hex_to_rgb(colores[-1])

    X, Y = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))
    Z = X
    color = np.zeros((Z.shape[0], Z.shape[1], 3))
    for i in range(Z.shape[0]):
        for j in range(Z.shape[1]):
            t = Z[i, j]  # Valor en el punto (i, j)
            color[i, j] = (1 - t) * color_start + t * color_end
    return color

def plot_ronda(Base, name):
    """
    Crea un gráfico con el torneo.

    Args:
    - Base 
    - name 
    """
    # Extraer coordenadas x, y y rutas de archivo
    
    x_coords = []
    y_coords = []
    fotos = []
    colors = []

    # Crear el gráfico de dispersión
    plt.figure(figsize=(10, 8))
    segmentos_pintados = set({})
    for i in Base:
        for j in i:
            if(i==0):
                continue
            x = j['x']
            y = j['y']
            y_hijo = j['yhijo']
            color = 'red' if j['win'] else 'black'
            segmento_x = [x-0.5,x-1] if x > 0 else [x+0.5,x+1]
            segmento_y = [y,y]
            plt.plot(segmento_x, segmento_y, linestyle='-', color = color)
            
            segmento_x = [x-1,x-1] if x > 0 else [x+1,x+1]
            segmento_y = [y,y_hijo]
            plt.plot(segmento_x, segmento_y, linestyle='-', color = color)
            
            segmento_x = (x-1,x-1.5) if x > 0 else (x+1,x+1.5)
            segmento_y = (y_hijo,y_hijo)
            if(j['win'] or abs(j['x']) == 2 or not((segmento_x,segmento_y)  in segmentos_pintados)):
                segmentos_pintados.add((segmento_x,segmento_y))
                plt.plot(segmento_x, segmento_y, linestyle='-', color = color)
            
            x_coords.append(j['x'])
            y_coords.append(j['y'])
            fotos.append(j['player']['foto'][:-4]+'.png')
            colors.append(matriz_color(j['player']['tipo']))

    

    # Iterar sobre los puntos y cargar las imágenes desde las rutas de archivo
    for x, y, foto,color in zip(x_coords, y_coords, fotos,colors):
        img = Image.open(foto)
        square = Rectangle((x - 0.5, y - 0.5), 1, 1, fill=False, edgecolor='black', zorder = 2)
        plt.gca().add_patch(square)
        plt.imshow(img, extent=(x - 0.5, x + 0.5, y - 0.5, y + 0.5), aspect='auto', zorder = 3)
        plt.imshow(color, extent=(x - 0.5, x + 0.5, y - 0.5, y + 0.5), aspect='auto', zorder = 1)
        

    # Ajustar los límites del gráfico para que se ajusten a los puntos
    limmax = max(max(x_coords), max(y_coords))+1
    plt.xlim(-limmax, limmax)
    plt.ylim(-limmax, limmax)

    # Guardar el gráfico en el archivo especificado
    plt.tight_layout()
    plt.axis('off')
    plt.text(0, limmax-4, f'Ronda: {name}', fontsize=24, fontweight='bold', ha='center',fontfamily='Comic Sans MS')
    save_path = os.path.join(save_folder, f'{name}.png')
    plt.savefig(save_path, dpi=300)
    #plt.show()

