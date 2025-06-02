import streamlit as st
import pandas as pd
import yfinance as yf

st.title("App Preço de Ações")

@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_acao = dados_acao.history(period="1d", start="2010-01-01", end="2024-07-01")
    cotacoes_acao = cotacoes_acao[["Close"]]
    return cotacoes_acao

# Nome correto do ticker, sem #
ticker = "ITUB4.SA"
dados = carregar_dados(ticker)

if dados.empty:
    st.error("Não foram encontrados dados para o ticker fornecido.")
else:
    st.write(f"O gráfico abaixo representa a evolução do preço das ações do {ticker} ao longo dos anos")
    st.line_chart(dados)

st.write("## Fim do app")
