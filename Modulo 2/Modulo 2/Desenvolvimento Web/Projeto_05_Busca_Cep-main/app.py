import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####
st.title("Buscar CEP")
st.image('principal.png')

##### Lista de Opções #####

opcoes = ["Buscar CEP", "Descobrir CEP"]



##### BARRA LATERAL #####
st.sidebar.image("logo.png")
opcoes = ["Buscar CEP", "Descobrir CEP"]
opcao = st.sidebar.selectbox("Voce quer", opcoes)

##### BOTÃO BUSCAR CEP #####
if opcao == "Buscar CEP":
   
    st.subheader('Buscar endereço pelo CEP')
    cep = st.text_input("Digiteo CEP (somente numeros)")

    if st.button("BUSCAR"):
        if len(cep) != 8 or not cep.isdigit():
            st.error("por favor, insira um cep valido ou verifique se contem 8 digitos:")
        else:
            try:
                endereco = BuscarCep.buscar_cep(cep)
                if endereco:
                    st.success("endereço encontrado:")
                    st.write(f"CEP: {endereco[0]}")
                    st.write(f"Endereço; {endereco[1]}")
                    st.write(f"Bairro: {endereco[2]}")
                    st.write(f"Cidade: {endereco[3]}")
                    st.write(f"Estado: {endereco[4]}")

                    #Mapas
                    st.title("Localização no Mapa")
                    df = pd.DataFrame({"latitude": [endereco[5]], "longitude": [endereco[6]]})
                    st.map(df, zoom = 15)
                else:
                    st.error("CEP não encontrado")
            except Exception as e:
                st.error(f"Ocorreu um erro ao buscar o CEP: {e}")



##### BOTÃO DESCOBRIR CEP #####
elif opcao == "Descobrir CEP":
    st.header("descobrir CEP pelo endereço:")
    endereco_usuario = st.text_input("digite o endereço (ex: Rua Olga,  Barueri, SP:")

    if st.button("descobrir"):
        if not endereco_usuario.strip():
            st.error("por favor, insira um endreço valido")
        else:
            try:
                resultado = BuscarCep.descobrir_cep(endereco_usuario)
                st.success("Link de busca no Google:")
                st.write(resultado)
            except Exception as e:
                st.error(f"ocorreu um erro ao descobrir o CEP: {e}")
                    
   