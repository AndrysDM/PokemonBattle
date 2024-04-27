import os
import matplotlib.pyplot as plt
from PIL import Image
ruta=os.getcwd()
fotourl=(os.path.join(ruta,'assets'))
fotourl=(os.path.join(fotourl,'Pokemon Grande'))
fotourl=(os.path.join(fotourl,'25.jpg'))

base=[[{'y': 0, 'x': 0, 'yhijo': 0, 'player': 8558}], [{'y': 0, 'x': 2, 'yhijo': 0, 'player': 8558}, {'y': 0, 'x': -2, 'yhijo': 0, 'player': 8548}], [{'y': 8, 'x': 4, 
'yhijo': 0, 'player': 8558}, {'y': -8, 'x': 4, 'yhijo': 0, 'player': 4714}, {'y': 8, 'x': -4, 'yhijo': 0, 'player': 8548}, {'y': -8, 'x': -4, 'yhijo': 0, 'player': 9778}], [{'y': 12, 'x': 6, 'yhijo': 8, 'player': 4886}, {'y': 4, 'x': 6, 'yhijo': 0, 'player': 8558}, {'y': -4, 'x': 6, 'yhijo': -8, 'player': 8656}, {'y': -12, 'x': 6, 'yhijo': 0, 'player': 4714}, {'y': 12, 'x': -6, 'yhijo': 8, 'player': 8548}, {'y': 4, 'x': -6, 'yhijo': 0, 'player': 1234}, {'y': -4, 'x': -6, 'yhijo': -8, 'player': 9778}, {'y': -12, 'x': -6, 'yhijo': 0, 'player': 7327}], [{'y': 14, 'x': 8, 'yhijo': 12, 'player': 6522}, {'y': 10, 'x': 8, 'yhijo': 0, 'player': 4886}, {'y': 6, 'x': 8, 'yhijo': 4, 'player': 8558}, {'y': 2, 'x': 8, 'yhijo': 0, 'player': 6752}, {'y': -2, 'x': 8, 'yhijo': -4, 'player': 8631}, {'y': -6, 'x': 8, 
'yhijo': 0, 'player': 8656}, {'y': -10, 'x': 8, 'yhijo': -12, 'player': 6304}, {'y': -14, 'x': 8, 'yhijo': 0, 'player': 4714}, {'y': 14, 'x': -8, 'yhijo': 12, 'player': 2155}, {'y': 10, 'x': -8, 'yhijo': 0, 'player': 8548}, {'y': 6, 'x': -8, 'yhijo': 4, 'player': 1234}, {'y': 2, 'x': -8, 'yhijo': 0, 'player': 8428}, {'y': 
-2, 'x': -8, 'yhijo': -4, 'player': 9778}, {'y': -6, 'x': -8, 'yhijo': 0, 'player': 9665}, {'y': -10, 'x': -8, 'yhijo': -12, 'player': 2271}, {'y': -14, 'x': -8, 
'yhijo': 0, 'player': 7327}], [{'y': 15, 'x': 10, 'player': 6522, 'yhijo': 14}, {'y': 13, 'x': 10, 'player': 5897}, {'y': 11, 'x': 10, 'player': 4886, 'yhijo': 10}, {'y': 9, 'x': 10, 'player': 8112}, {'y': 7, 'x': 10, 'player': 6250, 'yhijo': 6}, {'y': 5, 'x': 10, 'player': 8558}, {'y': 3, 'x': 10, 'player': 6752, 'yhijo': 2}, {'y': 1, 'x': 10, 'player': 8624}, {'y': -1, 'x': 10, 'player': 1531, 'yhijo': -2}, {'y': -3, 'x': 10, 'player': 8631}, {'y': -5, 'x': 10, 'player': 4761, 'yhijo': -6}, {'y': -7, 'x': 10, 'player': 8656}, {'y': -9, 'x': 10, 'player': 2590, 'yhijo': -10}, {'y': -11, 'x': 10, 'player': 6304}, {'y': -13, 'x': 10, 'player': 4714, 'yhijo': -14}, {'y': -15, 'x': 10, 'player': 6555}, {'y': 15, 'x': -10, 'player': 4468, 'yhijo': 14}, {'y': 13, 'x': -10, 'player': 2155}, {'y': 11, 'x': -10, 'player': 3814, 'yhijo': 10}, {'y': 9, 'x': -10, 'player': 8548}, {'y': 7, 'x': -10, 'player': 6915, 'yhijo': 6}, {'y': 5, 'x': -10, 'player': 1234}, {'y': 
3, 'x': -10, 'player': 8428, 'yhijo': 2}, {'y': 1, 'x': -10, 'player': 7330}, {'y': -1, 'x': -10, 'player': 9778, 'yhijo': -2}, {'y': -3, 'x': -10, 'player': 9451}, {'y': -5, 'x': -10, 'player': 9492, 'yhijo': -6}, {'y': -7, 'x': -10, 'player': 9665}, {'y': -9, 'x': -10, 'player': 2271, 'yhijo': -10}, {'y': -11, 'x': -10, 
'player': 3062}, {'y': -13, 'x': -10, 'player': 3218, 'yhijo': -14}, {'y': -15, 'x': -10, 'player': 7327}]]

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

    for i in Base:
        for j in i:
            x_coords.append(j['x'])
            y_coords.append(j['y'])
            fotos.append(fotourl)

    # Crear el gráfico de dispersión
    plt.figure(figsize=(10, 6))

    # Iterar sobre los puntos y cargar las imágenes desde las rutas de archivo
    for x, y, foto in zip(x_coords, y_coords, fotos):
        img = Image.open(foto)
        plt.imshow(img, extent=(x - 0.5, x + 0.5, y - 0.5, y + 0.5), aspect='auto')

    # Ajustar los límites del gráfico para que se ajusten a los puntos
    plt.xlim(min(x_coords) - 1, max(x_coords) + 1)
    plt.ylim(min(y_coords) - 1, max(y_coords) + 1)

    # Agregar título y etiquetas de ejes
    plt.title('Puntos con imágenes locales')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')

    # Guardar el gráfico en el archivo especificado
    plt.savefig(save_path)
    plt.show()

# Ejemplo de uso
save_path = 'puntos_con_imagenes_locales.png'
plot_points_with_local_images(base, 0)
