import streamlit as st

# Título y autor
st.title("Mi primera app")
st.write("Esta app fue elaborada por María Alejandra Echavarría Correa.")

# Pregunta al usuario por su nombre
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Mostrar mensaje de bienvenida
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
