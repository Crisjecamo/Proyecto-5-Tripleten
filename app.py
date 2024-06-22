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


disp_button = st.checkbox('Build scatter chart')

if disp_button:

    st.write('Create a scatter chart for your car sale ads dataset')

    fig = px.scatter(df, x='odometer')

    st.plotly_chart(fig, use_container_width=True)


table_checkbox = st.checkbox('Manufacturers with less than 1000 listings')

if table_checkbox:

    st.write('Create a table to visualize your car sale ads dataset')

    df1 = df[df['days_listed'] < 1000]

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df1.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df1.price, df1.model_year,
                           df1.model,
                           df1.condition, df1.cylinders,
                           df1.fuel, df1.odometer,
                           df1.transmission, df1.type,
                           df1.paint_color, df1.is_4wd,
                           df1.date_posted, df1.days_listed],
                   fill_color='lavender',
                   align='left'))
    ])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


general_info_button = st.button('Construct Gerenal Info')  # crear un botón

if general_info_button:

    st.write(
        'Creating a General info for the car sale ads dataset')

    # crear un histograma
    fig = px.scatter(df[df['days_listed'] < 1000], x="odometer", y="price",
                     size="model_year", color="type",
                     hover_data=["model", "model_year", "condition", "paint_color",
                                 "fuel", "cylinders", "is_4wd", "transmission"],)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
