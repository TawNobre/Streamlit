import streamlit as st
import random

lista_resposta = ["Ok", "Legal", "Olá", "Tem certeza?"]

def app():
    st.header("Chat teste")
    st.write("### Escreva e interaja com o chat ao vivo")

    if "mensagens" not in st.session_state:
        st.session_state["mensagens"] = []

    mensagem_usuario = st.chat_input("Digite a sua mensagem aqui!")

    if mensagem_usuario:
        mensagens = st.session_state["mensagens"]
        mensagens.append({"usuario": "user", "texto": mensagem_usuario})
        mensagens.append({"usuario": "assistente", "texto": "ok"})

    resposta = random.choice(lista_resposta)
    for mensagem in st.session_state["mensagens"]:
        with st.chat_message(mensagem["usuario"]):
            st.write(mensagem["texto"])

app()
