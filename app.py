import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('vehicles_us.csv')


'''Sustituimos los datos ausentes por un 0 en la columna "model_year" 
luego cambiamos el formato a int y por ultimo sustituimos los 0 por "unknown"
'''

df['model_year'] = df['model_year'].fillna(0)
df['model_year'] = df['model_year'].astype('int')

'''Sustituimos los datos ausentes por un 0 en la columna "cylinders" 
luego cambiamos el formato a int y por ultimo sustituimos los 0 por "unknown"
'''

df['cylinders'] = df['cylinders'].fillna(0)
df['cylinders'] = df['cylinders'].astype('int')
df['cylinders'] = df['cylinders'].replace(0, 'unknown')

'''En la columna "odometer" cambiamos el formato a int'''

df['odometer'] = df['odometer'].astype('Int64')

'''Sustituimos los datos ausentes por "unknown" en la columna "cylinders" '''

df['paint_color'] = df['paint_color'].fillna('unknown')

'''Sustituimos los datos ausentes por "unknown" en la columna "is_4wd" 
luego cambiamos el formato a object
'''

df['is_4wd'] = df['is_4wd'].fillna('unknown')
df['is_4wd'] = df['is_4wd'].astype('object')

'''cambiamos el formato de "date_posted" a datetime'''

df['date_posted'] = pd.to_datetime(df['date_posted'], format='%Y-%m-%d')


'''Hemos observado que habian datos en la columna model mal escritos 
se realiza la correccion de los mismos para obtener los datos correctamente
'''

df['model'] = df['model'].replace('ford f150', 'ford f-150')
df['model'] = df['model'].replace(
    'ford f250 super duty', 'ford f-250 super duty')
df['model'] = df['model'].replace('ford f350', 'ford f-350')


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
