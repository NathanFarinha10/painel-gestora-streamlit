# app.py

import streamlit as st

st.set_page_config(
    page_title="Painel de Visões de Mercado",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Bem-vindo ao Painel Consolidador de Visões de Mercado")

st.sidebar.success("Selecione uma das páginas acima para começar.")

st.markdown(
    """
    Este é um painel interativo projetado para centralizar e analisar as visões
    de mercado de grandes gestoras globais.

    **👈 Selecione na barra lateral o que você deseja fazer:**
    - **Dashboard Consolidado:** Para visualizar e filtrar as visões de mercado já processadas.
    - **Leitor de PDF:** Para fazer o upload de um novo relatório e extrair seu conteúdo textual.

    O próximo passo deste projeto é conectar a extração de texto do PDF com uma IA
    para popular o dashboard automaticamente.
    """
)
