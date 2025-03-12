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
    
    # Introdução
    st.markdown("""
    ### Introdução

    A escolha da linguagem de programação é essencial no desenvolvimento de software, pois afeta a produtividade, o aprendizado e as oportunidades no mercado. 
    Algumas linguagens se destacam por serem mais usadas e procuradas pelas empresas, influenciando tanto programadores quanto empregadores. 
    Nesse contexto, a análise de dados (Data Science) surge como uma ferramenta poderosa para identificar padrões e tendências no uso dessas linguagens, 
    auxiliando tanto desenvolvedores quanto empresas a tomar decisões mais informadas e estratégicas.

    Este estudo analisa as linguagens mais populares em 2024 e o perfil dos desenvolvedores, considerando experiência, tempo de prática e diversidade de conhecimento. 
    Com isso, buscamos entender padrões do mercado e como essas escolhas impactam a carreira dos profissionais e as necessidades das empresas. 
    A análise estatística e a aplicação de técnicas de Data Science permitirão extrair insights valiosos, como a relação entre experiência e produtividade, 
    a distribuição do tempo dedicado ao desenvolvimento e a popularidade das linguagens no cenário atual.
    """)

    # Apresentação dos Dados
    st.markdown("""
    ### 2. Apresentação dos Dados

    Os dados utilizados neste estudo foram obtidos a partir da pesquisa disponível no site **Statista**, que apresenta as linguagens de programação mais usadas por desenvolvedores de software em 2024. 
    Além disso, foi fornecida uma planilha contendo informações sobre **50 desenvolvedores**, incluindo a linguagem principal utilizada, anos de experiência, horas semanais dedicadas à programação e outras linguagens que conhecem.

    As variáveis presentes no conjunto de dados podem ser classificadas em dois tipos:

    - **Categóricas:** Linguagem principal, Linguagens Conhecidas.
    - **Numéricas:** Anos de experiência, Tempo Semanal (horas).

    A estrutura geral dos dados é organizada em colunas, sendo cada linha um desenvolvedor. O significado das colunas é:

    - **Desenvolvedor:** Identificação do profissional (Dev_001, Dev_002, etc.).
    - **Linguagem:** Linguagem de programação principal utilizada.
    - **Experiência (anos):** Tempo de experiência do desenvolvedor na linguagem principal.
    - **Tempo Semanal (horas):** Quantidade de horas semanais dedicadas à programação.
    - **Linguagens Conhecidas:** Outras linguagens que o desenvolvedor tem conhecimento.

    Essa base de dados permitirá a análise de padrões no mercado de desenvolvimento, relacionando o tempo de experiência com a escolha das linguagens, além de identificar tendências de uso e especialização.
    """)

    # Perguntas de Análise
    st.markdown("""
    ### 3. Perguntas de Análise

    #### 3.1 Quais são as linguagens mais utilizadas entre os desenvolvedores?
    Com base nos dados, as linguagens mais populares entre os desenvolvedores analisados são:

    - **Go** (13 desenvolvedores)
    - **C, Ruby, Rust, PowerShell e Bash/Shell** (12 desenvolvedores cada)
    - **PHP, SQL, Python** (11 desenvolvedores cada)

    Isso sugere uma grande diversidade na escolha de linguagens, sendo que algumas são mais amplamente adotadas.

    #### 3.2 Existe correlação entre anos de experiência e a quantidade de horas dedicadas por semana?
    Analisando as medidas estatísticas:

    - A média de anos de experiência é **11 anos**, com um desvio padrão de **6,69 anos**.
    - O tempo semanal médio dedicado ao desenvolvimento é **24,1 horas**, com um desvio padrão de **4,92 horas**.

    Os dados mostram uma variação significativa na experiência dos desenvolvedores e no tempo dedicado à programação, indicando que nem sempre há uma relação direta entre maior experiência e mais tempo de trabalho semanal.

    #### 3.3 Desenvolvedores com mais experiência tendem a conhecer mais linguagens?
    Embora os desenvolvedores mais experientes possam ter tido mais tempo para aprender novas linguagens, os dados sugerem que essa relação pode não ser tão forte. Por exemplo:

    - A moda da experiência foi **15 anos**, enquanto algumas das linguagens mais populares são usadas por desenvolvedores com diferentes níveis de experiência.
    - A distribuição das linguagens conhecidas sugere que a escolha pode estar mais relacionada ao contexto do trabalho e necessidades específicas do desenvolvedor.

    #### 3.4 A distribuição do tempo semanal dedicado ao desenvolvimento segue um padrão específico?
    A análise dos dados revela que:

    - A maioria dos desenvolvedores trabalha entre **20 e 30 horas semanais**, com um mínimo de **11 horas** e um máximo de **32 horas**.
    - A mediana indica que metade dos desenvolvedores dedica **25 horas ou menos** à programação por semana.

    Esses números sugerem que a carga horária segue uma distribuição relativamente normal, mas pode ser necessário um teste estatístico para confirmar essa hipótese.
    """)

    # Análises Estatísticas
    st.markdown("""
    ### 4. Análises Estatísticas

    #### 4.1 Medidas Descritivas

    ##### 4.1.1 Análise das Variáveis Numéricas
    Foram analisadas duas variáveis principais:

    - **Anos de experiência dos desenvolvedores.**
    - **Tempo semanal (horas) dedicado à programação.**

    Os cálculos estatísticos revelam os seguintes resultados:
    """)

    # Tabela de medidas descritivas
    medidas_descritivas = pd.DataFrame({
        "Métrica": ["Média", "Mediana", "Moda", "Desvio Padrão"],
        "Experiência (anos)": [11, 12, 15, 6.69],
        "Tempo Semanal (horas)": [24.1, 25, 31, 4.92]
    })
    st.dataframe(medidas_descritivas, hide_index=True, use_container_width=True)

    st.markdown("""
    **Interpretação:**

    - A média indica que a maioria dos desenvolvedores tem cerca de **11 anos de experiência** e trabalha **24,1 horas por semana**.
    - A mediana está próxima da média, sugerindo que os valores são distribuídos de maneira relativamente simétrica.
    - A moda da experiência é **15 anos**, indicando que há um número considerável de desenvolvedores nesse nível.
    - O desvio padrão alto para experiência (**6,69 anos**) mostra uma grande variação nos anos de atuação dos profissionais.
    """)

    st.markdown("""
    ##### 4.1.2 Distribuição das Linguagens Conhecidas
    A contagem das linguagens mais conhecidas pelos desenvolvedores mostrou que algumas são mais populares entre os profissionais:
    """)

    # Tabela de distribuição das linguagens
    linguagens_conhecidas = pd.DataFrame({
        "Linguagem": ["Go", "C", "Ruby", "Rust", "PowerShell", "Bash/Shell", "PHP", "SQL", "Python"],
        "Nº de Desenvolvedores": [13, 12, 12, 12, 12, 12, 11, 11, 11]
    })
    st.dataframe(linguagens_conhecidas, hide_index=True, use_container_width=True)

    st.markdown("""
    **Interpretação:**

    - Algumas linguagens aparecem com mais frequência, sugerindo que há uma tendência do mercado em utilizar múltiplas linguagens de programação, dependendo da necessidade do projeto.
    - Linguagens como **Go, C, Ruby, Rust, PowerShell e Bash/Shell** são amplamente adotadas pelos desenvolvedores na amostra analisada.
    """)

    st.markdown("""
    #### 4.2 Correlação e Dispersão
    Para entender a relação entre anos de experiência e tempo semanal de trabalho, calculamos o coeficiente de correlação de Pearson, que resultou em aproximadamente **-0,12**.

    **Interpretação:**

    - Esse valor sugere que **não há uma correlação forte** entre a experiência do desenvolvedor e o número de horas semanais trabalhadas.
    - O valor negativo pode indicar uma leve tendência de que desenvolvedores mais experientes trabalhem menos horas semanais, mas o efeito é muito fraco para ser conclusivo.

    Além disso, analisamos se desenvolvedores com mais experiência conhecem mais linguagens. Os dados mostraram que a média de linguagens conhecidas por desenvolvedor é de **2,5 linguagens**, e não há uma relação evidente entre anos de experiência e a quantidade de linguagens aprendidas.
    """)

    # Aplicação de Distribuições Estatísticas
    st.markdown("""
    ### 5. Aplicação de Distribuições Estatísticas

    #### 5.1 Distribuição Normal – Tempo Semanal de Programação
    Para verificar se o tempo semanal dedicado à programação segue uma distribuição normal, analisamos sua média (**24,1 horas**) e desvio padrão (**4,92 horas**).

    Para testar a normalidade, utilizamos o teste de Shapiro-Wilk, que obteve um p-valor inferior a **0,05**, indicando que os dados **não seguem uma distribuição normal**.

    **Interpretação:**

    - Apesar da média e da mediana estarem próximas (**24,1 horas** e **25 horas**, respectivamente), os dados apresentam uma leve assimetria.
    - O tempo dedicado à programação pode estar influenciado por fatores externos, como carga de trabalho, experiência e rotina dos desenvolvedores.
    - Como os dados não seguem uma normalidade perfeita, seria mais adequado utilizar uma distribuição diferente para modelá-los em uma análise preditiva.
    """)

    st.markdown("""
    #### 5.2 Distribuição Binomial ou Poisson – Número de Linguagens Conhecidas
    Para modelar a probabilidade de um desenvolvedor conhecer uma determinada linguagem, consideramos duas possíveis distribuições: **Binomial** e **Poisson**.

    - **Distribuição Binomial:** apropriada para eventos com duas possibilidades (sucesso ou fracasso), como "conhece ou não conhece uma linguagem".
    - **Distribuição de Poisson:** usada para modelar o número de ocorrências de um evento em um intervalo de tempo ou espaço, útil para contar quantas linguagens um desenvolvedor conhece.

    Após análise, a **Distribuição de Poisson** foi escolhida, pois o número de linguagens conhecidas segue um padrão de contagem discreta.

    O parâmetro **λ (média de linguagens conhecidas por desenvolvedor)** foi calculado como **2,5**. Assim, a probabilidade de um desenvolvedor conhecer exatamente **3 linguagens**, por exemplo, pode ser calculada pela fórmula da Poisson:
    """)

    # Fórmula da Poisson
    st.latex(r"""
    P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
    """)

    st.markdown("""
    Substituindo os valores:
    """)

    st.latex(r"""
    P(X = 3) = \frac{e^{-2.5} \cdot (2.5)^3}{3!} \approx 0.213
    """)

    st.markdown("""
    **Interpretação:**

    - Existe aproximadamente **21,3% de chance** de um desenvolvedor conhecer exatamente **3 linguagens**.
    - A distribuição mostra que a maioria dos desenvolvedores conhece entre **2 e 4 linguagens**, confirmando que a Poisson é uma boa modelagem para essa variável.
    """)

    # Conclusão
    st.markdown("""
    ### 6. Conclusão

    #### 6.1 Resumo das Principais Descobertas
    A análise dos dados revelou que **JavaScript, HTML/CSS e Python** são as linguagens mais utilizadas pelos desenvolvedores em 2024, com taxas de uso superiores a **50%**. Além disso, encontramos uma leve correlação entre anos de experiência e tempo semanal dedicado à programação, sugerindo que desenvolvedores mais experientes costumam manter uma carga de trabalho estável.

    Os cálculos estatísticos indicaram que o tempo médio semanal dedicado à programação é de **24,1 horas**, com um desvio padrão de **4,92 horas**. No entanto, os dados não seguem uma distribuição normal, o que sugere que diferentes fatores influenciam essa variável. Já a quantidade de linguagens conhecidas pelos desenvolvedores seguiu um comportamento próximo à **Distribuição de Poisson**, com uma média de **2,5 linguagens por desenvolvedor**.

    #### 6.2 Implicações para Empresas

    ##### Quais linguagens são essenciais para contratação?
    Empresas que buscam desenvolvedores devem priorizar candidatos com conhecimento em **JavaScript, HTML/CSS e Python**, pois essas são as linguagens mais populares e amplamente utilizadas. Além disso, **SQL e TypeScript** também aparecem com alta representatividade, o que indica sua importância no mercado.

    ##### Tempo médio esperado de dedicação de um profissional
    A carga horária semanal varia, mas a maioria dos desenvolvedores trabalha entre **20 e 30 horas semanais** em atividades de programação. Esse dado pode ser útil para empresas ajustarem expectativas e workload de suas equipes.

    #### 6.3 Implicações para Desenvolvedores

    ##### Quais linguagens são mais populares e valem a pena aprender?
    Para quem deseja ingressar na área de desenvolvimento, é recomendável aprender **JavaScript, HTML/CSS e Python**, pois são as mais utilizadas. Além disso, linguagens como **SQL e TypeScript** também aparecem com grande relevância no mercado.

    ##### Qual o tempo médio de experiência esperado para diferentes linguagens?
    Desenvolvedores que trabalham com linguagens mais antigas, como **C e Java**, tendem a ter maior experiência (em média **10 a 15 anos**). Por outro lado, linguagens como **Python e TypeScript** são amplamente usadas por profissionais iniciantes e com pouca experiência.
    """)

    # Upload e análise de dados
    # Carregar os dados diretamente da planilha
    try:
        # Caminho relativo para o arquivo Excel
        caminho_planilha = "desenvolvedores.xlsx"
        df = pd.read_excel(caminho_planilha)
        
        st.write("### Dados Carregados Automaticamente")
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
        else:
            st.warning("O arquivo não contém colunas numéricas para análise.")
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")