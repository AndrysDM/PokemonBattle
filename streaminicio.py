import streamlit as st
import os

def streaminicio():
    ruta=os.getcwd()
    ruta=os.path.join(ruta,'assets')
    volbasaur=os.path.join(ruta,'1.jpg')
    charmander=os.path.join(ruta,'4.jpg')
    squirte=os.path.join(ruta,'7.jpg')
    pokeball=os.path.join(ruta,'poke-ball.png')

    colp=st.columns(16)
    for i in colp:
        with i:
            st.image(pokeball)

    st.write(f'<div style="text-align:center;color:red;font-size:60px;font-family:cursive;">Pokemon Battle</div>',unsafe_allow_html=True)
    
    col=st.columns(3)
    with col[0]:
        st.image(volbasaur)
    with col[1]:
        st.image(charmander)
    with col[2]:
        st.image(squirte)
    
    
    st.write(f'<div style="text-align:center;color:#ff00ff;font-size:30px;font-family:cursive;">En esta pagina podras:</div>',unsafe_allow_html=True)
    html_string="""<p style="font-family:courier;color:green;text-algin:center">Lee con atencion:</p>
        <ul>
            <li> Simular un torneo pokemon
            <li> Ver la pokedex de Kanto
            <li> Darnos 5
        </ul>"""
    st.markdown(html_string,unsafe_allow_html=True)

    colp=st.columns(16)
    for i in colp:
        with i:
            st.image(pokeball)
    
    #st.write(f'<div style="text-align:center;color:red;font-size:40px;font-family:cursive;">Pokemon</div>',unsafe_allow_html=True)