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


# Esta línea crea un encabezado en la aplicación Streamlit con el texto “Vehicle Data Viewer”. Sirve como título para la sección o componente que sigue
st.header('Vehicle Data Viewer')

# Aquí se crea un botón con el texto “Create general data table”. Cuando el usuario hace clic en este botón, se activa la variable table_prueba_button
table_prueba_button = st.button('Create general data table')

# Esta línea verifica si el botón ha sido presionado (es decir, si table_prueba_button es verdadero). Si es así, se ejecuta el bloque de código que sigue.
if table_prueba_button:

    # Dentro del bloque condicional, se muestra un mensaje en la aplicación Streamlit que dice “Creating a table for the vehicle sale ads dataset”. Esto es opcional y se utiliza para proporcionar información adicional al usuario.
    st.write('Creating a table for the vehicle sale ads dataset')

    # Finalmente, se muestra un DataFrame llamado df en la aplicación Streamlit. Este DataFrame contiene datos relacionados con anuncios de venta de vehículos.
    st.dataframe(df)

################################################################################################

# Esta línea crea un encabezado en la aplicación Streamlit con el texto “Vehicle Data Graph”. Sirve como título para la sección o componente que sigue
st.header('Vehicle Data Graph')

# Aquí se crea un botón con el texto “Create a general data information graph”. Cuando el usuario hace clic en este botón, se activa la variable general_info_button
general_info_button = st.button(
    'Create a general data information graph')

# Esta línea verifica si el botón ha sido presionado (es decir, si table_prueba_button es verdadero). Si es así, se ejecuta el bloque de código que sigue.
if general_info_button:

    # Dentro del bloque condicional, se muestra un mensaje en la aplicación Streamlit que dice “Creating the Overview Chart for the Vehicle Sale Ads Dataset”. Esto es opcional y se utiliza para proporcionar información adicional al usuario.
    st.write(
        'Creating the Overview Chart for the Vehicle Sale Ads Dataset')

    # crear un grafico de dispersion
    fig = px.scatter(df, x="odometer", y="price",
                     size="model_year", color="type",
                     hover_data=["model", "model_year", "condition", "paint_color",
                                 "fuel", "cylinders", "is_4wd", "transmission"],)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

###############################################################################################

# Esta línea crea un encabezado en la aplicación Streamlit con el texto “Vehicle types by Manufacturer”. Sirve como título para la sección o componente que sigue
st.header('Vehicle types by Manufacturer')

# Aquí se crea un botón con el texto “Create a chart with the manufacturer and vehicle type”. Cuando el usuario hace clic en este botón, se activa la variable bar_button
bar_button = st.button('Create a chart with the manufacturer and vehicle type')

# Realizamos un Diccionario para filtrar cada vehiculo por marca
x = {
    'Toyota': df[df['model'].str.contains('toyota', case=False)],
    'Ford': df[df['model'].str.contains('ford', case=False)],
    'Hyundai': df[df['model'].str.contains('hyundai', case=False)],
    'Jeep': df[df['model'].str.contains('jeep', case=False)],
    'Dodge': df[df['model'].str.contains('dodge', case=False)],
    'Acura': df[df['model'].str.contains('acura', case=False)],
    'BMW': df[df['model'].str.contains('bmw', case=False)],
    'Cadillac': df[df['model'].str.contains('cadillac', case=False)],
    'Chrysler': df[df['model'].str.contains('chrysler', case=False)],
    'Honda': df[df['model'].str.contains('honda', case=False)],
    'Kia': df[df['model'].str.contains('kia', case=False)],
    'Chevrolet': df[df['model'].str.contains('chevrolet', case=False)],
    'Ram': df[df['model'].str.contains('ram', case=False)],
    'GMC': df[df['model'].str.contains('gmc', case=False)],
    'Nissan': df[df['model'].str.contains('nissan', case=False)],
    'Subaru': df[df['model'].str.contains('subaru', case=False)],
    'Mercedes-Benz': df[df['model'].str.contains('mercedes-benz', case=False)],

}

# Crear un DataFrame combinando los DataFrames filtrados

combined_df = pd.concat(x.values())

# Crear una nueva columna 'marca' con las claves del diccionario

combined_df['marca'] = combined_df['model'].apply(lambda model: next(
    (marca for marca, df_marca in x.items() if model in df_marca['model'].values), None))

# Calcular la cantidad de modelos por marca

model_count_by_marca = combined_df.groupby(
    ['marca', 'type'])['model'].count().reset_index()

# Esta línea verifica si el botón ha sido presionado (es decir, si bar_button es verdadero). Si es así, se ejecuta el bloque de código que sigue.
if bar_button:

    # Dentro del bloque condicional, se muestra un mensaje en la aplicación Streamlit que dice “Creating the Overview Chart for the Vehicle Sale Ads Dataset”. Esto es opcional y se utiliza para proporcionar información adicional al usuario.
    st.write('Creating Info manufacturer vehicle for the car sale ads dataset')

    # Crear el gráfico de barras con colores según el tipo de vehículo

    fig = px.bar(model_count_by_marca, x='marca', y='model',
                 color='type', title='Number of models by manufacturer')

    # Cambiar el nombre del eje 'y' a 'count'

    fig.update_yaxes(title_text='count')

    # Cambiar el nombre del eje x a 'manufacturer'

    fig.update_xaxes(title_text='manufacturer')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

############################################################################################

# Esta línea crea un encabezado en la aplicación Streamlit con el texto “Histogram of condition vs model year”. Sirve como título para la sección o componente que sigue
st.header('Histogram of condition vs model year')

# Realizamos el cambio de formato de nuestra columna a object simplemente remplazando 0 por 'unknown' para realizar el siguiente grafico
df['model_year'] = df['model_year'].replace(0, 'unknown')

# Aquí se crea un botón con el texto “Create a histogram of the condition vs the year of the vehicle”. Cuando el usuario hace clic en este botón, se activa la variable his_button
his_button = st.button(
    'Create a histogram of the condition vs the year of the vehicle')

# Esta línea verifica si el botón ha sido presionado (es decir, si bar_button es verdadero). Si es así, se ejecuta el bloque de código que sigue.
if his_button:

    # Dentro del bloque condicional, se muestra un mensaje en la aplicación Streamlit que dice “Creating the histogram”. Esto es opcional y se utiliza para proporcionar información adicional al usuario.
    st.write('Creating the histogram')

    # Crear el histograma con colores según la condicion del vehículo
    fig = px.histogram(df, x="model_year", color="condition")

    # Configuramos el rango del eje x
    fig.update_xaxes(range=[1920, 2020])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

##############################################################################

# Esta línea crea un encabezado en la aplicación Streamlit con el texto “Compare price distribution between manufacturer”. Sirve como título para la sección o componente que sigue
st.header('Compare price distribution between manufacturer')

# Aquí se crea un botón con el texto “Create a histogram of the price and the model of the vehiclecc”. Cuando el usuario hace clic en este botón, se activa la variable his_button
his_button = st.checkbox(
    'Create a histogram of the price and the model of the vehicle')

# Esta línea verifica si el botón ha sido presionado (es decir, si hist_button es verdadero). Si es así, se ejecuta el bloque de código que sigue.
if his_button:

    # Calcular la cantidad de modelos por marca

    df2 = combined_df.groupby(
        ['marca', 'price'])['model'].count().reset_index()

    # Crear los menús desplegables

    articulo1 = st.selectbox("Selecciona el artículo 1", df2['marca'].unique())

    articulo2 = st.selectbox("Selecciona el artículo 2", df2['marca'].unique())

    # Agrupamos los menus desplegables en el dataset
    df_filtrado = df2[df2['marca'].isin([articulo1, articulo2])]

    # Creamos el histograma con colores según la marca del vehículo
    fig = px.histogram(df_filtrado, x='price', color='marca',
                       title='Price distribution between vehicles')

    # mostrar un gráfico Plotlby interactivo
    st.plotly_chart(fig, use_container_width=True)
