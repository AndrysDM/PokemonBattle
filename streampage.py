import streamlit as st
from tools import obtener_fecha as day
from streamtoreno import streamtorneo
from streampokedeck import streampokedeck
from streamdesarrolladores import streamdesarolladores
from streaminicio import streaminicio
import os
def visual(inscritos,base,pokegrande,descalificados):
    def Inicio():
        streaminicio()

    def Torneo():
        streamtorneo(inscritos,base,descalificados)

    def Pokedex():
        streampokedeck(pokegrande)

    def Desarrolladores():
        streamdesarolladores()
    st.sidebar.title('Menu Pokemon')
    page=st.sidebar.selectbox('selecciona',['Inicio','Torneo','Pokedex','Desarrolladores'])
    
    ruta_imagen = os.path.join(os.getcwd(), 'assets')
    ruta_imagen = os.path.join(ruta_imagen, 'poke-ball.png')

    st.sidebar.image(ruta_imagen,width=200)


    if page=='Inicio':
        Inicio()
    elif page=='Torneo':
        Torneo()
    elif page=='Pokedex':
        Pokedex()
    else:
        Desarrolladores()