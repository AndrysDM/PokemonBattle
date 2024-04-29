import streamlit as st
import os

def torneo_pos_inscripcion(players,descalificados):
    if(len(descalificados)>0):
        st.markdown(
            f"""
            <div style='background-color: #ffffff; padding: 10px; border-radius: 10px;'>
                <h3 style='text-align: center; color: #333;'>Se han inscrito al torneo <span style='color: red;'>{len(players)+len(descalificados)}</span> Pokemones de los cuales se han descalificado <span style='color: red;'>{len(descalificados)}</span></h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        for i in range(len(descalificados)):
            if i%7==0:
                col = st.columns(7)
            with col[i%7]:
                st.image(descalificados[i][0])
        
        