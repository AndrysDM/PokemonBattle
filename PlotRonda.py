import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
ruta=os.getcwd()
fotourl=(os.path.join(ruta,'assets'))
fotourl=(os.path.join(fotourl,'Pokemon Grande'))
fotourl=(os.path.join(fotourl,'25.jpg'))

base=[[{'y': 0, 'x': 0, 'yhijo': 0, 'win': 0, 'player': 6497}], [{'y': 0, 'x': 2, 'yhijo': 0, 'win': 0, 'player': 6789}, {'y': 0, 'x': -2, 'yhijo': 0, 'win': 1, 'player': 6497}], [{'y': 8, 'x': 4, 'yhijo': 0, 'win': 1, 'player': 6789}, {'y': -8, 'x': 4, 'yhijo': 0, 'win': 0, 'player': 1718}, {'y': 8, 'x': -4, 'yhijo': 0, 'win': 1, 'player': 6497}, {'y': -8, 'x': -4, 'yhijo': 0, 'win': 0, 'player': 8473}], [{'y': 12, 'x': 6, 'yhijo': 8, 'win': 0, 'player': 1900}, {'y': 4, 'x': 6, 'yhijo': 8, 'win': 1, 'player': 6789}, {'y': -4, 'x': 6, 'yhijo': -8, 'win': 0, 'player': 8139}, {'y': -12, 'x': 6, 'yhijo': -8, 'win': 1, 'player': 1718}, {'y': 12, 'x': -6, 'yhijo': 8, 'win': 0, 'player': 4044}, {'y': 4, 'x': -6, 'yhijo': 8, 'win': 1, 'player': 6497}, {'y': -4, 'x': -6, 'yhijo': -8, 'win': 1, 'player': 8473}, {'y': -12, 'x': -6, 'yhijo': -8, 'win': 0, 'player': 3243}], [{'y': 14, 'x': 8, 'yhijo': 12, 'win': 0, 'player': 3784}, {'y': 10, 'x': 8, 'yhijo': 12, 'win': 1, 'player': 1900}, {'y': 6, 'x': 8, 'yhijo': 4, 'win': 1, 'player': 6789}, {'y': 2, 'x': 8, 'yhijo': 4, 'win': 0, 'player': 7149}, {'y': -2, 'x': 8, 'yhijo': -4, 'win': 1, 'player': 8139}, {'y': -6, 'x': 8, 'yhijo': -4, 'win': 0, 'player': 4669}, {'y': -10, 'x': 8, 'yhijo': -12, 'win': 0, 'player': 4660}, {'y': -14, 'x': 8, 'yhijo': -12, 'win': 1, 'player': 1718}, {'y': 14, 'x': -8, 'yhijo': 12, 'win': 0, 'player': 9207}, {'y': 10, 'x': -8, 'yhijo': 12, 'win': 1, 'player': 4044}, {'y': 6, 'x': -8, 'yhijo': 4, 'win': 0, 'player': 7167}, {'y': 2, 'x': -8, 'yhijo': 4, 'win': 1, 'player': 6497}, {'y': -2, 'x': -8, 'yhijo': -4, 'win': 1, 'player': 8473}, {'y': -6, 'x': -8, 'yhijo': -4, 'win': 0, 'player': 2335}, {'y': -10, 'x': -8, 'yhijo': -12, 'win': 0, 'player': 9646}, {'y': -14, 'x': -8, 'yhijo': -12, 'win': 1, 'player': 3243}], [{'y': 15, 'win': 1, 'x': 10, 'player': 3784, 'yhijo': 14}, {'y': 13, 'win': 0, 'x': 10, 'player': 2076, 'yhijo': 14}, {'y': 11, 'win': 
1, 'x': 10, 'player': 1900, 'yhijo': 10}, {'y': 9, 'win': 0, 'x': 10, 'player': 7463, 'yhijo': 10}, {'y': 7, 'win': 0, 'x': 10, 'player': 3518, 'yhijo': 6}, {'y': 5, 'win': 1, 'x': 10, 'player': 6789, 'yhijo': 6}, {'y': 3, 'win': 0, 'x': 10, 'player': 1997, 'yhijo': 2}, {'y': 1, 'win': 1, 'x': 10, 'player': 7149, 'yhijo': 
2}, {'y': -1, 'win': 1, 'x': 10, 'player': 8139, 'yhijo': -2}, {'y': -3, 'win': 0, 'x': 10, 'player': 1659, 'yhijo': -2}, {'y': -5, 'win': 1, 'x': 10, 'player': 4669, 'yhijo': -6}, {'y': -7, 'win': 0, 'x': 10, 'player': 8032, 'yhijo': -6}, {'y': -9, 'win': 1, 'x': 10, 'player': 4660, 'yhijo': -10}, {'y': -11, 'win': 0, 'x': 10, 'player': 6187, 'yhijo': -10}, {'y': -13, 'win': 1, 'x': 10, 'player': 1718, 'yhijo': -14}, {'y': -15, 'win': 0, 'x': 10, 'player': 2208, 'yhijo': -14}, {'y': 15, 'win': 1, 'x': -10, 'player': 9207, 'yhijo': 14}, {'y': 13, 'win': 0, 'x': -10, 'player': 1160, 'yhijo': 14}, {'y': 11, 'win': 0, 'x': -10, 'player': 7045, 'yhijo': 10}, {'y': 9, 'win': 1, 'x': -10, 'player': 4044, 'yhijo': 10}, {'y': 7, 'win': 0, 'x': -10, 'player': 5852, 'yhijo': 6}, {'y': 5, 'win': 1, 'x': -10, 'player': 7167, 'yhijo': 6}, {'y': 3, 'win': 0, 'x': -10, 'player': 5331, 'yhijo': 2}, {'y': 1, 'win': 1, 'x': -10, 'player': 6497, 'yhijo': 2}, {'y': -1, 'win': 0, 'x': -10, 'player': 6487, 'yhijo': -2}, {'y': -3, 'win': 1, 'x': -10, 'player': 8473, 'yhijo': -2}, {'y': -5, 'win': 0, 'x': -10, 'player': 2344, 'yhijo': -6}, 
{'y': -7, 'win': 1, 'x': -10, 'player': 2335, 'yhijo': -6}, {'y': -9, 'win': 1, 'x': -10, 'player': 9646, 'yhijo': -10}, {'y': -11, 'win': 0, 'x': -10, 'player': 
9131, 'yhijo': -10}, {'y': -13, 'win': 0, 'x': -10, 'player': 1119, 'yhijo': -14}, {'y': -15, 'win': 1, 'x': -10, 'player': 3243, 'yhijo': -14}]]
def plot_points_with_local_images(Base, i):
    """
    Crea un gráfico de dispersión de los puntos dados con imágenes cargadas desde rutas de archivo locales.

    Args:
    - points (list of tuples): Una lista de tuplas donde cada tupla contiene (x, y, ruta_de_archivo).
    - save_path (str): Ruta donde se guardará el gráfico generado.
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
            
            if(j['win']):
                segmento_x = [x-1,x-1.5] if x > 0 else [x+1,x+1.5]
                segmento_y = [y_hijo,y_hijo]
                plt.plot(segmento_x, segmento_y, linestyle='-', color = color)
            
            x_coords.append(j['x'])
            y_coords.append(j['y'])
            fotos.append(fotourl)

    

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

    # Agregar título y etiquetas de ejes
    # plt.title('Puntos con imágenes locales')
    # plt.xlabel('Coordenada X')
    # plt.ylabel('Coordenada Y')

    # Guardar el gráfico en el archivo especificado
    plt.tight_layout()
    plt.axis('off')
    plt.show()

# Ejemplo de uso
save_path = 'puntos_con_imagenes_locales.png'
plot_points_with_local_images(base, 0)
