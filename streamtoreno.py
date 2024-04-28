from torneoinscripcion import torneoinscripciones
import streamlit as st
from torneotorneo import torneotorneo
from torneowin import torneowin
def streamtorneo(inscritos, base):
    # Obtener el valor actual del contador
    contador = st.session_state.get("contador", 0)
    if contador == 0: 
        torneoinscripciones(inscritos)
    elif contador <= len(base)+1:
        torneotorneo(contador-1)
    else:
        torneowin(base[0][0]['player']['name'],base[0][0]['player']['foto'])

    # Función de devolución de llamada para actualizar el contador
    def actualizar_contador():
        nonlocal contador
        if(contador <= len(base)+1):
            contador += 1
        else:
            st.cache_data.clear()
            st.cache_resource.clear()
            contador = 0
        st.session_state.contador = contador
    def text_contador():
        if(contador == 0):
            return '🔥Empezar torneo!🔥'
        elif contador <= len(base):
            return '🔥Siguiente Ronda!🔥'
        elif contador == len(base)+1:
            return '🔥Mostrar Ganador🔥'
        else:
            return 'Reiniciar Torneo'
    # Mostrar el botón con el contador como nombre y la función de devolución de llamada
    col=st.columns(3)
    
    with col[1]:
        if st.button(text_contador(), on_click=actualizar_contador, ):
            pass  # No se necesita ninguna acción aquí
        
    # Llamar a la función torneoinscripciones con las inscripciones
    
