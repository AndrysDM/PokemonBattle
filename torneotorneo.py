import streamlit as st
import os

def torneotorneo(contador):
    st.image("./rondas_del_torneo/" + f'{contador}.png', use_column_width=True)
