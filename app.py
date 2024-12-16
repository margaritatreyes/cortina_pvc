import streamlit as st
import math

def calcular_tira_necesaria(alto_puerta, ancho_puerta, ancho_tira_cm, traslape_lado_cm):
    # Convertir el ancho de la tira y el traslape de cm a metros
    ancho_tira = ancho_tira_cm / 100
    traslape_lado = traslape_lado_cm / 100
    
    # Calcular el ancho efectivo de cada tira
    ancho_efectivo = ancho_tira - traslape_lado
    
    # Calcular la cantidad de tiras necesarias
    if ancho_puerta <= ancho_efectivo:
        tiras_necesarias = 1
    elif ancho_puerta <= ((2 * ancho_efectivo) + traslape_lado):
        tiras_necesarias = 2
    else :
        tiras_necesarias =  math.ceil((ancho_puerta - traslape_lado)/ ancho_efectivo)
    
    # Calcular la cantidad de metros lineales que se van en las tiras necesarias
    if tiras_necesarias <= 1:
        metro_lineal_tira = (tiras_necesarias * ancho_tira )
    else:
        metro_lineal_tira = (tiras_necesarias * ancho_efectivo ) + (traslape_lado)
    
    # Calcular la cantidad total de metros de tira necesarios
    metros_necesarios = tiras_necesarias * alto_puerta

    return tiras_necesarias, metro_lineal_tira, metros_necesarios



def redondear_a_multiplo_de_5(valor):
    # Redondear hacia arriba al múltiplo de 5 más cercano
    return math.ceil(valor / 5) * 5


st.title("Calculadora de Metros de Cortina PVC")
st.markdown("Tiras de 20cm: ")
st.markdown("El traslape de las tiras de 20cm son de (3.6cm = 36%) y (7.5cm = 75%) en las bases metalicas #4334 ")
st.markdown("El traslape de las tiras de 20cm son de (4.2cm = 42%) y (9.2cm = 92%) en las bases metalicas #4335 ")
st.markdown("Tiras de 30cm: ")
st.markdown("Nota: El traslape de las tiras de 30cm son de (9.7cm = 64%) en las bases metalicas #4334 ")
st.markdown("Nota: El traslape de las tiras de 30cm son de (10.4cm = 69%) en las bases metalicas #4335 ")



# Entrada del alto y ancho de la puerta & del ancho de la tira y traslape
alto_puerta = st.number_input("Alto de la puerta (metros):", min_value=0.0, format="%.2f")
ancho_puerta = st.number_input("Ancho de la puerta (metros):", min_value=0.0, format="%.2f")
ancho_tira = st.number_input("Ancho de la tira (cm):", min_value=0.0, format="%.2f")
traslape_lado = st.number_input("Traslape por lado (cm):", min_value=0.0, format="%.2f")

if st.button("Calcular"):
    tiras_necesarias, metro_lineal_tira, metros_necesarios = calcular_tira_necesaria(alto_puerta, ancho_puerta, ancho_tira, traslape_lado)

    # Redondear los resultados al múltiplo de 5 más cercano
    metros_necesarios_redondeado = redondear_a_multiplo_de_5(metros_necesarios)

    st.write(f"Metros de cortina necesarios (redondeado al múltiplo de 5): {metros_necesarios_redondeado} metros.")
    st.write(f"Metros de cortina necesarios (sin redondear): {metros_necesarios:.2f} metros.")
    st.write(f"Tiras necesarias: {tiras_necesarias} tiras.")
    st.write(f"Longitud total de las tiras en metros: {metro_lineal_tira:.3f} metros.")   
