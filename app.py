import streamlit as st

def calcular_cortina(alto_puerta, ancho_puerta, ancho_producto, traslape):
    traslape_metros = traslape / 100
    ancho_efectivo = ancho_producto - traslape_metros
    tiras_necesarias = ancho_puerta / ancho_efectivo
    metros_necesarios = tiras_necesarias * alto_puerta
    return metros_necesarios

st.title("Calculadora de Cortina Plástica")

alto_puerta = st.number_input("Alto de la puerta (m):", min_value=0.0, format="%.2f")
ancho_puerta = st.number_input("Ancho de la puerta (m):", min_value=0.0, format="%.2f")
traslape = st.number_input("Traslape (cm):", min_value=0.0, format="%.2f")

if st.button("Calcular"):
    result_20cm = calcular_cortina(alto_puerta, ancho_puerta, 0.2, traslape)
    result_30cm = calcular_cortina(alto_puerta, ancho_puerta, 0.3, traslape)

    st.write(f"Ancho del producto: 20 cm: {result_20cm:.2f} metros de cortina necesarios")
    st.write(f"Ancho del producto: 30 cm: {result_30cm:.2f} metros de cortina necesarios")
