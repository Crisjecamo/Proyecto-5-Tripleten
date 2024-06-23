import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('vehicles_us.csv')


# Sustituimos los datos ausentes por un 0 en la columna "model_year"
# luego cambiamos el formato a int y por ultimo sustituimos los 0 por "unknown"


df['model_year'] = df['model_year'].fillna(0)
df['model_year'] = df['model_year'].astype('int')

# Sustituimos los datos ausentes por un 0 en la columna "cylinders"
# luego cambiamos el formato a int y por ultimo sustituimos los 0 por "unknown"


df['cylinders'] = df['cylinders'].fillna(0)
df['cylinders'] = df['cylinders'].astype('int')
df['cylinders'] = df['cylinders'].replace(0, 'unknown')

# En la columna "odometer" cambiamos el formato a int

df['odometer'] = df['odometer'].astype('Int64')

# Sustituimos los datos ausentes por "unknown" en la columna "cylinders" '''

df['paint_color'] = df['paint_color'].fillna('unknown')

# Sustituimos los datos ausentes por "unknown" en la columna "is_4wd"
# luego cambiamos el formato a object

df['is_4wd'] = df['is_4wd'].fillna('unknown')
df['is_4wd'] = df['is_4wd'].astype('object')

# cambiamos el formato de "date_posted" a datetime

df['date_posted'] = pd.to_datetime(df['date_posted'], format='%Y-%m-%d')


# Hemos observado que habian datos en la columna model mal escritos
# se realiza la correccion de los mismos para obtener los datos correctamente


df['model'] = df['model'].replace('ford f150', 'ford f-150')
df['model'] = df['model'].replace(
    'ford f250 super duty', 'ford f-250 super duty')
df['model'] = df['model'].replace('ford f350', 'ford f-350')


##############################################################################


st.header('Vehicle Data Viewer')

table_prueba_button = st.button('Create general data table')

if table_prueba_button:

    st.write('Creating a table for the vehicle sale ads dataset')

    st.dataframe(df)

################################################################################################

st.header('Vehicle Data Graph')

general_info_button = st.button(
    'Create a general data information graph')  # crear un botón

if general_info_button:

    st.write(
        'Creating the Overview Chart for the Vehicle Sale Ads Dataset')

    # crear un histograma
    fig = px.scatter(df, x="odometer", y="price",
                     size="model_year", color="type",
                     hover_data=["model", "model_year", "condition", "paint_color",
                                 "fuel", "cylinders", "is_4wd", "transmission"],)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

###############################################################################################

st.header('Vehicle types by Manufacturer')

bar_button = st.button('Create a chart with the manufacturer and vehicle type')

if bar_button:

    st.write('Creating Info manufacturer vehicle for the car sale ads dataset')

    x = {
        'Toyota': df[df['model'].str.contains('toyota', case=False)],
        'Ford': df[df['model'].str.contains('ford', case=False)],
        'Hyundai': df[df['model'].str.contains('hyundai', case=False)],
        'Jeep': df[df['model'].str.contains('jeep', case=False)],
        'Dodge': df[df['model'].str.contains('dodge', case=False)],
    }

    # Crear un DataFrame combinando los DataFrames filtrados

    combined_df = pd.concat(x.values())

    # Crear una nueva columna 'marca' con las claves del diccionario

    combined_df['marca'] = combined_df['model'].apply(lambda model: next(
        (marca for marca, df_marca in x.items() if model in df_marca['model'].values), None))

    # Calcular la cantidad de modelos por marca

    model_count_by_marca = combined_df.groupby(
        ['marca', 'type'])['model'].count().reset_index()

    # Crear el gráfico de barras con colores según el tipo de vehículo

    fig = px.bar(model_count_by_marca, x='marca', y='model',
                 color='type', title='Cantidad de modelos por fabricante')

    # Cambiar el nombre del eje 'y' a 'count'

    fig.update_yaxes(title_text='count')

    # Cambiar el nombre del eje x a 'manufacturer'

    fig.update_xaxes(title_text='manufacturer')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

############################################################################################

st.header('Histogram of condition vs model year')

df['model_year'] = df['model_year'].replace(0, 'unknown')

his_button = st.button(
    'Create a histogram of the condition vs the year of the vehicle')

if his_button:

    st.write('Creating the histogram')

    fig = px.histogram(df, x="model_year", color="condition")

    fig.update_xaxes(range=[1920, 2020])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

##############################################################################

st.header('Histogram of condition vs model year')

his_button = st.checkbox(
    'Create a histogram of the condition vs the year of the vehicle')

if his_button:

    df2 = combined_df.groupby(
        ['marca', 'price'])['model'].count().reset_index()

    # Crear los menús desplegables

    articulo1 = st.selectbox("Selecciona el artículo 1", df2['marca'])

    articulo2 = st.selectbox("Selecciona el artículo 2", df2['marca'])

    df_filtrado = df2[df2['marca'].isin([articulo1, articulo2])]

    fig = px.bar(df_filtrado, x='marca', y='price', color='marca',
                 title='Comparación de precios entre artículos')

    st.plotly_chart(fig, use_container_width=True)
