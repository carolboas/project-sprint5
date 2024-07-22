import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')  # lendo os dados
hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um cabeçalho
    st.header('Histograma de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x='odometer')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Criar um gráfico de dispersão')  # criar um botão

if scatter_button:  # se o botão for clicado
    # escrever ua mensagem
    st.write('Criando um um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um cabeçalho
    st.header('Gráfico de dispersão de dados de anúncios de vendas de carros')

    # criar um gráfico de dispersão
    chart = px.scatter(car_data, x='odometer')

    # exibir um gráfico plotly interativo
    st.plotly_chart(chart, use_container_width=True)
