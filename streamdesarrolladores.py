import streamlit as st
import os
import time

def streamdesarolladores():

    # Título de la página
    st.markdown("<h1 style='text-align: center; color: #FF4533;'>Creado por:</h1>", unsafe_allow_html=True)    
    # Nombres de los desarrolladores
    st.markdown("<h3 style='text-align: center;'>- Domínguez Moreno A. -</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>- Ferrer Leyva O. -</h2>", unsafe_allow_html=True)


    # Cargar imagen    
    st.write(' ')
    col=st.columns(3)
    ruta_imagen = os.path.join(os.getcwd(), 'assets')
    with col[0]:
        st.image(os.path.join(ruta_imagen,'master-ball.jpg'))
    ruta_imagen = os.path.join(ruta_imagen, 'Pokemon Grande')
    ruta_imagen = os.path.join(ruta_imagen, '10.png')
    with col[2]:
        st.image(ruta_imagen)
