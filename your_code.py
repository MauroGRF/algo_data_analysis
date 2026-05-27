import pandas as pd

""" Cargar el marco de datos """
df = pd.read_csv ('GoogleApps.csv')


""" ¿Cuál es el nombre de la primera aplicación en el conjunto de datos? """
fist_app = df["App"][0] #Obtener la primera posición de un dataframe

""" ¿A qué categoría pertenece la última aplicación del conjunto de datos? """
last_app = df["App"].iloc()

""" ¿Cuántas columnas hay en el conjunto de datos? """
check_columns = df.shape[0] # Para obtener el encabezado

""" ¿Cuántas filas hay en el conjunto de datos? """
check_rows = df.shape[1] # Para obtener el numero de filas

""" Informacion general sobre el DataFrame procesado (A nivel terminal/consola) """
df.info() # Muestra en el conjunto de datos

""" Especifique la media aritmética y la mediana del tamaño de la aplicación (Tamaño) """
mean_sizeapp = df["Size"].mean() # Tamaño promedio entre todas aplicaciones
median_sizeapp = df["Size"].median() # Tamaño el cual se acerca la mitad de aplicaciones

""" ¿Cuánto cuesta la aplicación más cara? """
cost_app = df["Price"].max()

""" Especifique la media aritmética y la mediana del número de instalaciones de aplicaciones (Instalaciones) """
mean_downloadsapp = df["Installs"].mean() # Descarga promedio entre todas aplicaciones
median_downloadsapp = df["Installs"].median() # Descarga el cual se acerca la mitad de aplicaciones


while True:
    print("Elija una opción:")
    print("""
    1- ¿Cuál es el nombre de la primera aplicación en el conjunto de datos?
    2- ¿A qué categoría pertenece la última aplicación del conjunto de datos?
    3- ¿Cuántas columnas hay en el conjunto de datos?
    4- ¿Cuántas filas hay en el conjunto de datos?
    5- ¿Qué tipo de datos se almacenan en cada una de las columnas?
    6- Especifique la media aritmética y la mediana del tamaño de la aplicación (Tamaño) 
    7- ¿Cuánto cuesta la aplicación más cara?
    8- Especifique la media aritmética y la mediana del número de instalaciones de aplicaciones (Instalaciones)
    9- Salir
    """)

    print("-"*100)
    opc = input("Opción:")
    match opc:
        case "1":
            print(fist_app)
        case "2":
            print(last_app)
        case "3":
            print(check_columns)
        case "4":
            print(check_rows)
        case "5":
            print(df.info())
        case "6":
            print("Tamaño promedio entre todas aplicaciones", mean_sizeapp)
            print("Tamaño el cual se acerca la mitad de aplicaciones", median_sizeapp)
        case "7":
            print(cost_app)
        case "8":
            print("Descargas promedio entre todas aplicaciones",mean_downloadsapp)
            print("Descargas el cual se acerca la mitad de aplicaciones", median_downloadsapp)
        case "9":
            break
        case _:
            print("Opción no válida")
    
    print("-"*100)

