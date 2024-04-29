import tools as tools
import os
import streamlit as st
ruta=os.getcwd()
ruta=os.path.join(ruta,'assets')
pkgrandes=tools.inicializar_fotos(os.path.join(ruta,'Pokemon Grande'))

from ponerfondo import generar_fotos_fondo
import Torneo as tor
#jugadores que pasaran a players2 con <foto,nombre,tipo>:
from inscripcion import inscripciones
#inscritos en fechas que pasara a inscritos2 <dia,<<foto,nombre,tipo>>,<>,<>>:
#from inscripcion import inscritos

from GenerarPlotsRonda import GenerarPlotsRonda

import streampage as mi_st

@st.cache_data
def generar_datos():
	players, inscritos = inscripciones()
	tools.revolver(players)
	descalificados=[]
	tor.descalificar(players,descalificados)
	print('Presine para empezar el torneo')
	
	players2=tools.Tplayers(players,pkgrandes)
	
	descalificados=tools.Tplayers(descalificados,pkgrandes)
	
	inscritos2=tools.Tinscrip(inscritos,pkgrandes)

	base=tor.torneo(players2)
	GenerarPlotsRonda(base)
	#print(inscritos2)
	generar_fotos_fondo(players2)
	generar_fotos_fondo(descalificados)
	print("el ganador es: ")
	print(base[0][0])
	return inscritos2,base,players2,descalificados

def main():
	st.set_page_config(
		page_title="Pokemon Battle",
		page_icon="./assets/icono.png",
		initial_sidebar_state="collapsed"
	)
	inscritos2,base,players2 ,descalificados =generar_datos()
	mi_st.visual(inscritos2,base,pkgrandes, players2 ,descalificados)
	#los resultados del torneo quedan guardados en 'base'
	

if __name__=='__main__':
	main()