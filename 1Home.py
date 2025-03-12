import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotnine import *

# Configuração da página
st.set_page_config(page_title="Dashboard de Distribuições Probabilísticas", layout="wide")

# Criando as sub-abas (pages)
pages = st.sidebar.selectbox("Escolha a sua seção:", [
    "Quem sou eu?",
    "Formação e Experiências Profissionais",
    "Skills",
    "Contato",
    "Análise de Dados"
])

st.sidebar.markdown("Desenvolvido por Miguel Parrado")

if pages == "Quem sou eu?":
    st.header("Quem sou eu?")
    
    st.image("e43b602a-d5b1-40b8-a0b7-fcae39e1e060.webp", width=600)

    st.write("""
    Sou estudante do 4º semestre de Engenharia de Software na FIAP, em São Paulo, Brasil.
    Meu foco principal é o desenvolvimento backend, buscando aprimorar minhas habilidades e atuar na construção de sistemas robustos e eficientes.
    Tenho conhecimentos em React, Java, JavaScript e Python.
    Meu objetivo de carreira é trabalhar com backend em projetos escaláveis e inovadores.
    """)

elif pages == "Formação e Experiências Profissionais":
    st.header("Formação e Experiências Profissionais")
    st.write("""
    **Graduação:** Engenharia de Software - FIAP (Previsão de conclusão: 2027)

    **Projetos Acadêmicos:**
    - Implementação de algoritmos de ordenação em Python, analisando eficiência e desempenho.
    - Desenvolvimento de aplicações web utilizando React e Node.js.
    - Estudo e aplicação do Domain Driven Design em Java.
    """)

elif pages == "Skills":
    st.header("Skills")
    st.image("capa-linguagens-em-alta.webp", width=600)
    st.write("""
    **Linguagens e Ferramentas:**
    - Java, JavaScript, Python, React, SQL, GitHub, API REST, Banco de Dados

    **Soft Skills:**
    - Trabalho em equipe, resolução de problemas, comunicação eficaz

    **Habilidades do Setor:**
    - Desenvolvimento backend, arquitetura de software, padrões de projeto, metodologia ágil (Squad Framework, Scrum)
    """)

elif pages == "Contato":
    st.header("Contato")
    st.write("""
    **GitHub:** github.com/seuusuario

    **LinkedIn:** linkedin.com/in/seuusuario

    **E-mail:** miguelmpp12@gmail.com
    """)

elif pages == "Análise de Dados":
    st.header("Análise de Dados")
    st.write("Faça upload do seu arquivo Excel para analisar a distribuição de uma variável numérica.")
    uploaded_file = st.file_uploader("Carregue seu arquivo Excel", type=["xlsx", "xls"])
    
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Amostra dos dados:")
        st.write(df.head())
        
        colunas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
        if colunas_numericas:
            coluna_escolhida = st.selectbox("Escolha uma coluna numérica:", colunas_numericas)
            
            if coluna_escolhida:
                st.write("Distribuição dos dados:")
                st.write(df[coluna_escolhida].describe())
                
                dist = st.selectbox("Escolha a distribuição para análise:", ["Poisson", "Normal", "Binomial"])
                
                if dist == "Poisson":
                    lambda_est = df[coluna_escolhida].mean()
                    x = np.arange(0, 2 * lambda_est)
                    y = stats.poisson.pmf(x, lambda_est)
                    st.write("Distribuição de Poisson")
                    fig = go.Figure(data=[go.Bar(x=x, y=y)])
                    st.plotly_chart(fig)
                
                elif dist == "Normal":
                    mu_est = df[coluna_escolhida].mean()
                    sigma_est = df[coluna_escolhida].std()
                    x = np.linspace(mu_est - 4*sigma_est, mu_est + 4*sigma_est, 100)
                    y = stats.norm.pdf(x, mu_est, sigma_est)
                    st.write("Distribuição Normal")
                    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')])
                    st.plotly_chart(fig)
                
                elif dist == "Binomial":
                    n = 10  # número de tentativas fixo
                    p = df[coluna_escolhida].mean() / max(df[coluna_escolhida])
                    x = np.arange(0, n + 1)
                    y = stats.binom.pmf(x, n, p)
                    st.write("Distribuição Binomial")
                    fig = go.Figure(data=[go.Bar(x=x, y=y)])
                    st.plotly_chart(fig)
