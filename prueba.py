import streamlit as st
import time
a="Esto es una prueba sin nada."

st.write("Esto es una prueba con st.write")
a

#Ocultar el menú y el footer
hide_streamlit_style  = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)




#Título
st.title("Ejemplo v2")

#Input de texto
Texto  = st.text_input('Escribe aquí', '')

#Un área de texto
Contenido = st.text_area('Contenido:', "")

#Una simple lista
options = st.multiselect(
    "Opciones disponibles: ",
    ["Opción a", "Opción b", "Opción c"])

#Botón, cuando sea pulsado.
if st.button("Dale!"):
    print ("esto sale por la consola")
    my_bar = st.progress(0)

    #Barra de progreso
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
    #Cuadro texto verde
    st.success("El texto es " + Texto + " El contenido es:\n" + Contenido + "\n y las opciones son: " + str(options), icon="✅")

#Botón cuando no esté pulsado.
else:
    st.write("")
