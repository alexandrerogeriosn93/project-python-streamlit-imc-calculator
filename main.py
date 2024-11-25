import streamlit as st

st.title("Calculadora de IMC")

weight = st.number_input("Digite o seu peso em Kg")
height_scale = st.radio("Selecione a opção de altura", ("centímetros", "metros"))
height = st.number_input(f"Digite a altura em {height_scale}")

if st.button("Calcular IMC"):
    try:
        match height_scale:
            case "centímetros":
                imc = weight / ((height / 100) ** 2)
            case "metros":
                imc = weight / height**2
        st.text("O seu IMC é {:.2f}".format(imc))
    except ZeroDivisionError:
        st.error("Impossível divisão por zero.")
    except ValueError:
        st.error("Valor inválido.")
