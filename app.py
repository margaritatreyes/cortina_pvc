import streamlit as st

def calcular_cortina(alto_puerta, ancho_puerta, ancho_producto, porcentaje_traslape):
    # Calcular el traslape en metros basado en el porcentaje seleccionado
    traslape = ancho_producto * (porcentaje_traslape / 100)
    # Calcular el ancho efectivo de cada tira de cortina plástica
    ancho_efectivo = ancho_producto - traslape
    # Calcular la cantidad de tiras necesarias se agrega ancho puerta + translape porque representa el porcentaje de la primera y segunda tira sin translape
    tiras_necesarias = ((ancho_puerta *100) + traslape) / ancho_efectivo
    # Calcular la cantidad total de metros de cortina plástica necesarios
    metros_necesarios = tiras_necesarias * (alto_puerta * 100)
    return metros_necesarios

st.title("Calculadora de Cortina Plástica")

alto_puerta = st.number_input("Alto de la puerta (metros):", min_value=0.0, format="%.2f")
ancho_puerta = st.number_input("Ancho de la puerta (metros):", min_value=0.0, format="%.2f")

# Seleccionar el porcentaje de traslape
porcentaje_traslape = st.selectbox("Selecciona el porcentaje de traslape:", [25, 37, 50, 75])

if st.button("Calcular"):
    result_20cm = calcular_cortina(alto_puerta, ancho_puerta, 20, porcentaje_traslape)
    result_30cm = calcular_cortina(alto_puerta, ancho_puerta, 30, porcentaje_traslape)

    st.write(f"Ancho del producto: 20 cm: {result_20cm:.2f} metros de cortina necesarios")
    st.write(f"Ancho del producto: 30 cm: {result_30cm:.2f} metros de cortina necesarios")