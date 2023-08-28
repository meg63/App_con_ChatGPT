import streamlit as st

def conversion_temperatura():
    opciones = ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", opciones)

    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0

    if seleccion == "Celsius a Fahrenheit":
        resultado = valor * 9/5 + 32
    elif seleccion == "Fahrenheit a Celsius":
        resultado = (valor - 32) * 5/9
    elif seleccion == "Celsius a Kelvin":
        resultado = valor + 273.15
    elif seleccion == "Kelvin a Celsius":
        resultado = valor - 273.15

    st.write(f"Resultado: {valor} {seleccion.split(' ')[0]} es igual a {resultado:.2f} {seleccion.split(' ')[-1]}")

def conversion_longitud():
    opciones = ["Pies a Metros", "Metros a Pies", "Pulgadas a Centímetros", "Centímetros a Pulgadas"]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", opciones)

    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0

    if seleccion == "Pies a Metros":
        resultado = valor * 0.3048
    elif seleccion == "Metros a Pies":
        resultado = valor / 0.3048
    elif seleccion == "Pulgadas a Centímetros":
        resultado = valor * 2.54
    elif seleccion == "Centímetros a Pulgadas":
        resultado = valor / 2.54

    st.write(f"Resultado: {valor} {seleccion.split(' ')[0]} es igual a {resultado:.2f} {seleccion.split(' ')[-1]}")

def conversion_peso_masa():
    opciones = ["Libras a Kilogramos", "Kilogramos a Libras", "Onzas a Gramos", "Gramos a Onzas"]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", opciones)

    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0

    if seleccion == "Libras a Kilogramos":
        resultado = valor * 0.453592
    elif seleccion == "Kilogramos a Libras":
        resultado = valor / 0.453592
    elif seleccion == "Onzas a Gramos":
        resultado = valor * 28.3495
    elif seleccion == "Gramos a Onzas":
        resultado = valor / 28.3495

    st.write(f"Resultado: {valor} {seleccion.split(' ')[0]} es igual a {resultado:.2f} {seleccion.split(' ')[-1]}")

def conversion_volumen():
    opciones = ["Galones a Litros", "Litros a Galones", "Pulgadas cúbicas a Centímetros cúbicos", "Centímetros cúbicos a Pulgadas cúbicas"]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", opciones)

    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0

    if seleccion == "Galones a Litros":
        resultado = valor * 3.78541
    elif seleccion == "Litros a Galones":
        resultado = valor / 3.78541
    elif seleccion == "Pulgadas cúbicas a Centímetros cúbicos":
        resultado = valor * 16.3871
    elif seleccion == "Centímetros cúbicos a Pulgadas cúbicas":
        resultado = valor / 16.3871

    st.write(f"Resultado: {valor} {seleccion.split(' ')[0]} es igual a {resultado:.2f} {seleccion.split(' ')[-1]}")

def conversion_tiempo():
    opciones = ["Horas a Minutos", "Minutos a Segundos", "Días a Horas", "Semanas a Días"]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", opciones)

    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0

    if seleccion == "Horas a Minutos":
        resultado = valor * 60
    elif seleccion == "Minutos a Segundos":
        resultado = valor * 60
    elif seleccion == "Días a Horas":
        resultado = valor * 24
    elif seleccion == "Semanas a Días":
        resultado = valor * 7

    st.write(f"Resultado: {valor} {seleccion.split(' ')[0]} es igual a {resultado:.2f} {seleccion.split(' ')[-1]}")

def conversion_velocidad():
    opciones = ["Millas por hora a Kilómetros por hora", "Kilómetros por hora a Metros por segundo", "Nudos a Millas por hora", "Metros por segundo a Pies por segundo"]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", opciones)

    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0

    if seleccion == "Millas por hora a Kilómetros por hora":
        resultado = valor * 1.60934
    elif seleccion == "Kilómetros por hora a Metros por segundo":
        resultado = valor * 0.277778
    elif seleccion == "Nudos a Millas por hora":
        resultado = valor * 1.15078
    elif seleccion == "Metros por segundo a Pies por segundo":
        resultado = valor * 3.28084

    st.write(f"Resultado: {valor} {seleccion.split(' ')[0]} es igual a {resultado:.2f} {seleccion.split(' ')[-1]}")

def conversion_area():
    opciones = ["Metros cuadrados a Pies cuadrados", "Pies cuadrados a Metros cuadrados", "Kilómetros cuadrados a Millas cuadradas", "Millas cuadradas a Kilómetros cuadrados"]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", opciones)

    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0

    if seleccion == "Metros cuadrados a Pies cuadrados":
        resultado = valor * 10.7639
    elif seleccion == "Pies cuadrados a Metros cuadrados":
        resultado = valor / 10.7639
    elif seleccion == "Kilómetros cuadrados a Millas cuadradas":
        resultado = valor * 0.386102
    elif seleccion == "Millas cuadradas a Kilómetros cuadrados":
        resultado = valor / 0.386102

    st.write(f"Resultado: {valor} {seleccion.split(' ')[0]} es igual a {resultado:.2f} {seleccion.split(' ')[-1]}")

def conversion_energia():
    opciones = ["Julios a Calorías", "Calorías a Kilojulios", "Kilovatios-hora a Megajulios", "Megajulios a Kilovatios-hora"]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", opciones)

    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0

    if seleccion == "Julios a Calorías":
        resultado = valor * 0.239006
    elif seleccion == "Calorías a Kilojulios":
        resultado = valor / 0.239006
    elif seleccion == "Kilovatios-hora a Megajulios":
        resultado = valor * 1000
    elif seleccion == "Megajulios a Kilovatios-hora":
        resultado = valor / 1000

    st.write(f"Resultado: {valor} {seleccion.split(' ')[0]} es igual a {resultado:.2f} {seleccion.split(' ')[-1]}")

def conversion_presion():
    opciones = ["Pascales a Atmósferas", "Atmósferas a Pascales", "Barras a Libras por pulgada cuadrada", "Libras por pulgada cuadrada a Barras"]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", opciones)

    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0

    if seleccion == "Pascales a Atmósferas":
        resultado = valor / 101325
    elif seleccion == "Atmósferas a Pascales":
        resultado = valor * 101325
    elif seleccion == "Barras a Libras por pulgada cuadrada":
        resultado = valor * 14.5038
    elif seleccion == "Libras por pulgada cuadrada a Barras":
        resultado = valor / 14.5038

    st.write(f"Resultado: {valor} {seleccion.split(' ')[0]} es igual a {resultado:.2f} {seleccion.split(' ')[-1]}")

def conversion_datos():
    opciones = ["Megabytes a Gigabytes", "Gigabytes a Terabytes", "Kilobytes a Megabytes", "Terabytes a Petabytes"]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", opciones)

    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0

    if seleccion == "Megabytes a Gigabytes":
        resultado = valor / 1024
    elif seleccion == "Gigabytes a Terabytes":
        resultado = valor / 1024
    elif seleccion == "Kilobytes a Megabytes":
        resultado = valor / 1024
    elif seleccion == "Terabytes a Petabytes":
        resultado = valor / 1024

    st.write(f"Resultado: {valor} {seleccion.split(' ')[0]} es igual a {resultado:.2f} {seleccion.split(' ')[-1]}")

def main():
    st.title("Conversor Universal")

    categorias = [
        "Temperatura", "Longitud", "Peso/Masa", "Volumen",
        "Tiempo", "Velocidad", "Área", "Energía", "Presión", "Tamaño de Datos"
    ]
    categoria_seleccionada = st.selectbox("Selecciona una categoría:", categorias)

    if categoria_seleccionada == "Temperatura":
        conversion_temperatura()
    elif categoria_seleccionada == "Longitud":
        conversion_longitud()
    elif categoria_seleccionada == "Peso/Masa":
        conversion_peso_masa()
    elif categoria_seleccionada == "Volumen":
        conversion_volumen()
    elif categoria_seleccionada == "Tiempo":
        conversion_tiempo()
    elif categoria_seleccionada == "Velocidad":
        conversion_velocidad()
    elif categoria_seleccionada == "Área":
        conversion_area()
    elif categoria_seleccionada == "Energía":
        conversion_energia()
    elif categoria_seleccionada == "Presión":
        conversion_presion()
    elif categoria_seleccionada == "Tamaño de Datos":
        conversion_datos()

if __name__ == "__main__":
    main()
