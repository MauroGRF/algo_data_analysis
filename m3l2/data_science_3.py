import pandas as pd
df = pd.read_csv('GoogleApps.csv')

df.info()
print(df.head())
# 1 ¿Cuántas aplicaciones hay en la 'Category' 'BUSINESS' 'Category'?
categorias = df["Category"].value_counts()
print(categorias["BUSINESS"])


# 2 ¿Cuál es la relación de aplicaciones para adolescentes ('Teen') y las destinadas para niños mayores de 10 años ('Everyone 10+')?
# Redondee la respuesta a la centésima más cercana.
related = df["Content Rating"].value_counts()
print(round(related["Teen"] / related["Everyone 10+"],2))

# 
# 3.1 ¿Cuál es el 'Rating' promedio de aplicaciones 'Paid'? 
# Redondee la respuesta a la centésima más cercana.
paid_rating_mean = df[df["Type"] == "Paid"]["Rating"].mean()
print(round(paid_rating_mean,2))

# 3.2 ¿Cuánto más bajo es el 'Rating' promedio de aplicaciones 'Free' que el promedio de valoración de las aplicaciones 'Paid'?
# Redondee la respuesta a la centésima más cercana.
free_rating_mean = df[df["Type"] == "Free"]["Rating"].mean()
print(round(paid_rating_mean/free_rating_mean,2))

# 4 ¿Cuál es el 'Size' (tamaño) mínimo y máximo en la 'Category' 'COMICS'?
# Redondee la respuesta a la centésima más cercana.
comics = df[df["Category"] == "COMICS"]
print(comics["Size"].agg(min, max))


# Bonificación 1. ¿Cuántas aplicaciones tienen un 'Rating' estrictamente superior a 4.5 en la 'Category' 'FINANCE'?

# Bonificación 2. ¿Cuál es la relación de juegos 'Free' y 'Paid' con un 'Rating' superior a 4.9?


