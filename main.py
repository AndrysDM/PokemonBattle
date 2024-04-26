import tools as tools
import os
ruta=os.getcwd()
ruta=os.path.join(ruta,'assets')
pkgrandes=tools.inicializar_fotos(os.path.join(ruta,'Pokemon Grande'))
pkchiquito=tools.inicializar_fotos(os.path.join(ruta,'Pokemon Chiquito'))

import Torneo as tor
from inscripcion import players 

	

def main():
	
	tools.revolver(players)
	tor.descalificar(players)
	print('Presine para empezar el torneo')
	input()
	base=tor.torneo(players)
	print("\nEl ganador es ",base[0][0])
	#los resultados del torneo quedan guardados en 'base'
	

if __name__=='__main__':
	main()