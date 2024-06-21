import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Vehicle Data Viewer')

hist_button = st.button('Construct histogram')  # crear un botón

if hist_button:

    st.write(
        'Creating a histogram for the car sale ads dataset')

    # crear un histograma
    fig = px.histogram(df, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Build scatter chart')

if disp_button:

    st.write('Create a scatter chart for your car sale ads dataset')

    fig = px.scatter(df, x='odometer')

    st.plotly_chart(fig, use_container_width=True)
