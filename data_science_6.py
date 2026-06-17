import pandas as pd

df = pd.read_csv('GoogleApps.csv')
# Imprimir información sobre todo el DataFrame para ver qué columnas hay que limpiar
print(df.info())

print(df["Installs"])

# ¿Cuántas aplicaciones en el conjunto de datos no tienen ('NaN') clasificación ('Rating')?
df_rating= df['Rating'] # Obteniendo serie Rating
nulls_rating = pd.isnull(df_rating) # devuelve la serie de datos que son NaN
df_empty_rating = df[nulls_rating]
print(len(df_empty_rating))

df_mean_rating = df_rating.median()

# Reemplazar el valor nulo ('NaN') de la clasificación ('Rating') para tales aplicaciones con -1.
df['Rating'].fillna(-1, inplace = True)

# df['Rating'].fillna(df_mean_rating, inplace = True) si quieren de alguna manera salvar los datos sin que se vean afectados por un 0


# Determinar qué otro valor de tamaño ('Size') se almacena en el conjunto de datos además de Kilobytes y Megabytes, y reemplazar por -1.
# Convertir los tamaños ('Size') de aplicación a formato numérico (float). Los tamaños de todas las aplicaciones deben medirse en Megabytes.
print(df['Size'].value_counts())


def set_size(size):
   if size[-1] == 'M':
      return float(size[:-1])
   elif size[-1] == 'k':
      return float(size[:-1]) / 1024
   return -1

df['Size'] = df['Size'].apply(set_size)


# ¿Cuál es el tamaño máximo 'Size' de las aplicaciones en 'Category' 'TOOLS'?
print(df[df['Category'] == 'TOOLS']['Size'].max())


# Tareas adicionales
# Reemplazar el tipo de datos por entero (int) para el número de instalaciones ('Installs').
# En la entrada del número de instalaciones ('Installs'), el signo "+" debe ser ignorado.
# Esto significa que si el número de instalaciones en el conjunto de datos es 1,000,000+, necesita cambiar el valor a 1000000
def set_installs(installs):
   if installs == '0':
       return 0
   return int(installs[:-1].replace(',', ''))

df['Installs'] = df['Installs'].apply(set_installs)


# Agrupar los datos por tipo ('Type') y público objetivo ('Content Rating') como prefiera,
# calcular el número promedio de instalaciones ('Installs') para cada grupo Redondear la respuesta a la centésima más cercana.
# En la tabla resultante, encontrar la celda con el mayor valor.
# ¿A qué grupo de edad y tipo de aplicación pertenecen los datos de esa celda?
print(round(df.pivot_table(index = 'Content Rating', columns = 'Type', values = 'Installs', aggfunc = 'mean')), 1)


# ¿Qué aplicación no tiene un 'Type' especificado? ¿Qué tipo debe introducirse allí en función del precio?
print(df[pd.isnull(df['Type'])])
# Puede usar iloc[0] para ver todas las columnas en lugar de la elipsis.
# print(df[pd.isnull(df['Type'])].iloc[0])
df['Type'].fillna('Free', inplace = True)


# Imprimir información sobre todos los DataFrames para asegurarse de que la limpieza se ha realizado con éxito
print(df.info())


