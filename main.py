import tools as tools
import os
ruta=os.getcwd()
ruta=os.path.join(ruta,'assets')
pkgrandes=tools.inicializar_fotos(os.path.join(ruta,'Pokemon Grande'))
pkchiquito=tools.inicializar_fotos(os.path.join(ruta,'Pokemon Chiquito'))

import Torneo as tor
#jugadores que pasaran a players2 con <foto,nombre,tipo>:
from inscripcion import players
#inscritos en fechas que pasara a inscritos2 <dia,<<foto,nombre,tipo>>,<>,<>>:
from inscripcion import inscritos

from GenerarPlotsRonda import GenerarPlotsRonda

def main():
	tools.revolver(players)
	tor.descalificar(players)
	print('Presine para empezar el torneo')
	input()

	players2=tools.Tplayers(players,pkgrandes)
	print(players2)
	inscritos2=tools.Tinscrip(inscritos,pkgrandes)

	base=tor.torneo(players2)
	GenerarPlotsRonda(base)

	#los resultados del torneo quedan guardados en 'base'
	

if __name__=='__main__':
	main()