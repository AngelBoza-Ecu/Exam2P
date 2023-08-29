#Import libraries

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import plotly_express as px
from PIL import Image


#Insertar icono de la app
icon =Image.open('Resources/logo_app.jpg')

#Configurar la página
st.set_page_config(page_title='Historial de Producción', page_icon=icon)


#Añadir markdown
st.markdown("""This is an app that helps you visualize the IPR curve and make 
calculations
"""
)

#Añadir título de la app
st.title('Historial de Producción')

#Añadir info adicional
expander = st.expander('Information about the Field')
expander.write("This field produced for around 8 years operated by Equinor")

#Añadir imagen
image =Image.open('Resources/Image_1.png')
st.image(image,width=100,use_column_width=True)

#Sidebar
st.sidebar.title('Functions')

#Menú
with st.sidebar:options = \
    option_menu(menu_title="Funtions' Menu",
                options=['Home','Data','Plots'],
                icons=['house','clipboard-data','box'],
    )

#Subir archivo
file = st.sidebar.file_uploader('Upload you .xlsx file')
#Mostrar dataframe
def data(dataframe):
    st.subheader("Field's Data")
    st.write(dataframe.head())
    st.subheader('Summary')
    st.write(dataframe.describe())

def plots(volvefield):
    Volo = volvefield['BORE_OIL_VOL']
    # Volg = volvefield['BORE_GAS_VOL']
    time = volvefield['DATEPRD']
    fig, ax = plt.subplots(figsize=(20, 10))
    x = time
    y = Volo
    # Build the curve
    ax.plot(x, y, c='g')
    ax.set_xlabel('t(años)', fontsize=14)
    ax.set_ylabel('Volo', fontsize=14)
    ax.set_title('Volo vs t(años)', fontsize=18)

    ax.grid()
    plt.show()

#Call data

if file:
    df =pd.read_excel(file)

    if options == 'Data':
        data(df)
    elif options == 'Plots':
        plots(data())


