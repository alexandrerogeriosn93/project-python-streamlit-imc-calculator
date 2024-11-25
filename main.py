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

        if imc < 16:
            st.error("Extremamente abaixo do peso")
        elif imc < 18.5:
            st.warning("Abaixo do peso")
        elif imc < 25:
            st.success("Saudável")
        elif imc < 30:
            st.warning("Acima do peso")
        else:
            st.error("Extremanete acima do peso")
    except ZeroDivisionError:
        st.error("Impossível divisão por zero.")
    except ValueError:
        st.error("Valor inválido.")
