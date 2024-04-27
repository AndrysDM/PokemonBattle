import streamlit as st
from tools import asignar_colores_a_tipos as pintar
import pandas as pd
import os

def convertir(p):
    u=''
    for i in p:
        if(i=='/'):
            break
        u+=i
    return u

def streampokedeck(pokegrande):
    st.title('Poke:red[dex]')
    st.write('Aqui podemos ver la pokedex de Kanto.')
    pintura=pintar()

    rutai=os.getcwd()
    rutdatos=(os.path.join(rutai,'assets'))
    rutdatos=(os.path.join(rutdatos,'arreglado.csv'))
    datos=pd.read_csv(rutdatos)
    
    
    a=st.number_input('Ingrese el menor:',value=1,step=1,min_value=1,max_value=151)
    b=st.number_input('Ingrese el mayor:',value=1,step=1,min_value=1,max_value=151)

    a-=1
    left,right=st.columns(2)
    for i in range(a,b):
        with left:
            st.image(pokegrande[i+1],caption=datos.iloc[i,2])
        with right:
            st.write(' ')
            st.write(' ')
            st.write(f'<div style="text-align:center;color:{pintura[convertir(datos.iloc[i,2])]};font-size:20px;font-family:cursive;">{datos.iloc[i,1]}</div>',unsafe_allow_html=True)
            st.write(' ')
            st.write(datos.iloc[i,3])
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')

            
           
    # st.write(f'<div style="text-align:center>datos.iloc[i,1]</div>',unsafe_allow_html=True)

        