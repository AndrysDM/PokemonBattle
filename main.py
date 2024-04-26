import tools as tools
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