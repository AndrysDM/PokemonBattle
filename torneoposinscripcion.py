import streamlit as st
import os

def torneo_pos_inscripcion(players,descalificados):
    resolucion=7
    if(len(descalificados)>0):
        st.markdown(
            f"""<div style='background-color: #ffeaea; padding: 10px; border-radius: 10px;'>
              <h2 style='text-align: center; color: #ff66a0;'>
                ❌Que mal❌
              </h2>
              <h3 style='text-algin: center; color: #992121;'>
                Los siguientes 
                <span style='color: #cc3535;'>
                  {len(descalificados)}
                </span>
                pokemones fueron descalificados
              </h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        #ajustar tama;o
        if(len(descalificados)<10):
            resolucion=3
        elif(len(descalificados)<16):
            resolucion=5
        else:
            resolucion=7

        #printear descalificados
        st.write(' ')
        for i in range(len(descalificados)):
            if i%resolucion==0:
                col = st.columns(resolucion)
            with col[i%resolucion]:
                st.image(descalificados[i][0],caption=descalificados[i][1])
    
    #lo mismo para los calificados
    st.write(' ')
    st.markdown(
            f"""<div style='background-color: #eaffea; padding: 10px; border-radius: 10px;'>
              <h2 style='text-align: center; color: #a0ff66;'>
                ✅Listos para la batalla✅
              </h2>
              <h3 style='text-algin: center; color: #219921;'>
                Los siguientes 
                  <span style='color: #35cc35;'>{len(players)}</span> 
                pokemones estan listos para el torneo
              </h3>
            </div>
            """,
            unsafe_allow_html=True
        )
    #ajustar tama;o
    if(len(players)<10):
        resolucion=3
    elif(len(players)<16):
        resolucion=5
    else:
        resolucion=7

    #printear clasificados
    st.write(' ')
    for i in range(len(players)):
        if i%resolucion==0:
            col = st.columns(resolucion)
        with col[i%resolucion]:
            st.image(players[i][0],caption=players[i][1])
        




    #    <h3 style='text-align: center; color: #333;'>Que mal <span style='color: red;'>{len(players)+len(descalificados)}</span> Pokemones de los cuales se han descalificado <span style='color: red;'>{len(descalificados)}</span></h3>