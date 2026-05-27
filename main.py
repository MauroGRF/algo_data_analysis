import streamlit as st
import pandas as pd

def main():

    data = pd.read_csv("GoogleApps.csv")


    # Configuración de la página
    st.title("Prueba de streamlit")
    st.header(":blue[Hola]")
    st.text("Hola")
    st.write("""
        ## Soporte con MarkDown (md).

        puedes[/color] escribir en formato MarkDown con Streamlit.
        - **Streamlit** Es $muy$ usado para Analisis de datos, por lo que es util para este modulo
        ``
        print("hola")
        ``
    """)

    st.dataframe(data)

if __name__ == "__main__":
    main()

