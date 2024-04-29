import streamlit as st
from tools import obtener_fecha as day
def torneoinscripciones(inscritos):
    st.markdown("<h1 style='text-align: center; color: #FF1120;'>⚔️Torneo⚔️</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #000000;'>📆Proceso de inscripcion:📆</h3>", unsafe_allow_html=True)
    for dia in inscritos:
        st.write('El dia',day(dia[0]) ,'se inscribieron',len(dia[1]))
        fotos=[]
        for pk in dia[1]:
            fotos.append(pk[0])
        col=st.columns(len(dia[1]))
        print(col)
        for i in range(0,len(dia[1])):
            with col[i]:
                st.image(fotos[i],caption=dia[1][i][1])

