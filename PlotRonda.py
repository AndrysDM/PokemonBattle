import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
ruta=os.getcwd()
fotourl=(os.path.join(ruta,'assets'))
save_folder=(os.path.join(ruta,'rondas_del_torneo'))
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

    # Crear el gráfico de dispersión
    plt.figure(figsize=(10, 8))

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
            
            if(j['win'] or abs(j['x']) == 2):
                segmento_x = [x-1,x-1.5] if x > 0 else [x+1,x+1.5]
                segmento_y = [y_hijo,y_hijo]
                plt.plot(segmento_x, segmento_y, linestyle='-', color = color)
            
            x_coords.append(j['x'])
            y_coords.append(j['y'])
            fotos.append(j['player']['foto'])

    

    # Iterar sobre los puntos y cargar las imágenes desde las rutas de archivo
    for x, y, foto in zip(x_coords, y_coords, fotos):
        img = Image.open(foto)
        square = Rectangle((x - 0.5, y - 0.5), 1, 1, fill=False, edgecolor='black')
        plt.gca().add_patch(square)
        plt.imshow(img, extent=(x - 0.5, x + 0.5, y - 0.5, y + 0.5), aspect='auto')
        

    # Ajustar los límites del gráfico para que se ajusten a los puntos
    limmax = max(max(x_coords), max(y_coords))+1
    plt.xlim(-limmax, limmax)
    plt.ylim(-limmax, limmax)

    # Guardar el gráfico en el archivo especificado
    plt.tight_layout()
    plt.axis('off')
    save_path = os.path.join(save_folder, f'{name}.png')
    plt.savefig(save_path)
    #plt.show()

