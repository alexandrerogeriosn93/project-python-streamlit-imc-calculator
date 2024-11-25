import streamlit as st

st.title("Calculadora de IMC")

weight = st.number_input("Digite o seu peso em Kg")
height_scale = st.radio("Selecione a opção de altura", ("centímetros", "metros"))
height = st.number_input(f"Digite a altura em {height_scale}")
