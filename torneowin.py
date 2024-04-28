import streamlit as st

def torneowin(nombre_ganador, url_foto_ganador):
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>¡Felicidades, campeón!</h1>", unsafe_allow_html=True)
    st.write(f"<h2 style='text-align: center;'>¡{nombre_ganador} ha ganado!</h2>", unsafe_allow_html=True)

    st.image(url_foto_ganador, caption=nombre_ganador, use_column_width=True)

    st.success("¡Gran trabajo! 🎉🏆🥳")
    st.balloons()