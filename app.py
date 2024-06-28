import streamlit as st
import math

def calcular_metros_tira(alto_puerta, ancho_puerta, ancho_tira_cm, traslape_lado_cm):
    # Convertir el ancho de la tira y el traslape de cm a metros
    ancho_tira = ancho_tira_cm / 100
    traslape_lado = traslape_lado_cm / 100
    # Calcular el ancho efectivo de cada tira
    ancho_efectivo = ancho_tira - traslape_lado
    # Calcular la cantidad de tiras necesarias
    tiras_necesarias = math.ceil(ancho_puerta / (ancho_tira - traslape_lado))
    # Calcular la cantidad de metros lineales que se van en las tiras necesarias
    if tiras_necesarias <= 1:
        metro_lineal_tira = (tiras_necesarias * ancho_tira )
    elif tiras_necesarias == 2:
        metro_lineal_tira = (tiras_necesarias * ancho_tira ) - traslape_lado
    else:
        metro_lineal_tira = (tiras_necesarias * (ancho_tira - traslape_lado)) + (traslape_lado)

    # Calcular la cantidad total de metros de tira necesarios
    metros_necesarios = tiras_necesarias * alto_puerta
    return tiras_necesarias, metros_necesarios, metro_lineal_tira

def redondear_a_multiplo_de_5(valor):
    # Redondear hacia arriba al múltiplo de 5 más cercano
    return math.ceil(valor / 5) * 5

st.title("Calculadora de Metros de Cortina PVC")

# Entrada del alto y ancho de la puerta
alto_puerta = st.number_input("Alto de la puerta (metros):", min_value=0.0, format="%.2f")
ancho_puerta = st.number_input("Ancho de la puerta (metros):", min_value=0.0, format="%.2f")

# Entrada del ancho de la tira y traslape
ancho_tira = st.number_input("Ancho de la tira (cm):", min_value=0.0, format="%.2f")
traslape_lado = st.number_input("Traslape por lado (cm):", min_value=0.0, format="%.2f")

if st.button("Calcular"):
    tiras_necesarias, metros_necesarios, metro_lineal_tira = calcular_metros_tira(alto_puerta, ancho_puerta, ancho_tira, traslape_lado)
    
    # Redondear los resultados al múltiplo de 5 más cercano
    metros_necesarios_redondeado = redondear_a_multiplo_de_5(metros_necesarios)

    st.write(f"Metros de cortina necesarios (sin redondear): {metros_necesarios:.2f} metros.")
    st.write(f"Metros de cortina necesarios (redondeado al múltiplo de 5 más cercano): {metros_necesarios_redondeado} metros.")
    st.write(f"Metros lineales en tiras: {metro_lineal_tira:.2f} metros.")   
    st.write(f"Tiras necesarias: {tiras_necesarias} tiras.")
