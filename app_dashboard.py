# app_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Painel Consolidador de Visões de Mercado")

# Carregar os dados (usamos cache para performance)
@st.cache_data
def carregar_dados():
    try:
        df = pd.read_csv('dados_manuais.csv')
        df['data_relatorio'] = pd.to_datetime(df['data_relatorio'])
        return df
    except FileNotFoundError:
        st.error("Arquivo 'dados_manuais.csv' não foi encontrado no repositório do GitHub.")
        return pd.DataFrame() # Retorna um dataframe vazio para evitar erros

df = carregar_dados()

if not df.empty:
    # --- BARRA LATERAL COM FILTROS ---
    st.sidebar.header("Filtros")

    # Filtro de Gestora
    gestoras_disponiveis = sorted(df['gestora'].unique())
    gestoras_selecionadas = st.sidebar.multiselect(
        'Selecione a(s) Gestora(s):', 
        options=gestoras_disponiveis, 
        default=gestoras_disponiveis
    )

    # Filtro de Classe de Ativo
    classes_disponiveis = sorted(df['classe_ativo'].unique())
    classes_selecionadas = st.sidebar.multiselect(
        'Selecione a(s) Classe(s) de Ativo:', 
        options=classes_disponiveis, 
        default=classes_disponiveis
    )

    # Aplicar filtros no DataFrame
    df_filtrado = df[
        df['gestora'].isin(gestoras_selecionadas) & 
        df['classe_ativo'].isin(classes_selecionadas)
    ]

    # --- EXIBIÇÃO DOS DADOS ---
    st.header("Visões Consolidadas")
    st.dataframe(df_filtrado)

    # --- VISUALIZAÇÕES GRÁFICAS ---
    if not df_filtrado.empty:
        st.header("Análise Gráfica")

        # Gráfico de contagem de visões por classe de ativo
        fig = px.bar(
            df_filtrado.groupby(['classe_ativo', 'visao']).size().reset_index(name='contagem'),
            x='classe_ativo',
            y='contagem',
            color='visao',
            title='Contagem de Visões por Classe de Ativo',
            barmode='group',
            color_discrete_map={
                'Overweight': '#2ca02c', # verde
                'Neutral': '#7f7f7f',    # cinza
                'Underweight': '#d62728' # vermelho
            },
            labels={'classe_ativo': 'Classe de Ativo', 'contagem': 'Número de Gestoras', 'visao': 'Visão'}
        )
        st.plotly_chart(fig, use_container_width=True)
