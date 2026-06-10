import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 ¿Cuántas aplicaciones hay en la 'Category' 'BUSINESS'?
""" Agrupación """
categorias = df["Category"].value_counts()
print(categorias)
print("-"*40)
print(categorias["BUSINESS"])

# 2 ¿Cuál es la relación de aplicaciones para adolescentes ('Teen') y las destinadas para niños mayores de 10 años ('Everyone 10+')?
# Redondee la respuesta a la centésima más cercana.
content_rating = df["Content Rating"].value_counts()
cr_teen = content_rating["Teen"]
cr_everyone = content_rating["Everyone 10+"]
print(round(cr_teen/cr_everyone, 2))

# 3.1 ¿Cuál es el 'Rating' promedio de aplicaciones 'Paid'? 
# Redondee la respuesta a la centésima más cercana.
apps_paid = df[df["Type"] == "Paid"] 
mean_apps_paid = apps_paid["Rating"].mean()
print(round(mean_apps_paid,2))


# 3.2 ¿Cuánto más bajo es el 'Rating' promedio de aplicaciones 'Free' que el promedio de valoración de las aplicaciones 'Paid'?
# Redondee la respuesta a la centésima más cercana.
apps_free = df[df["Type"] == "Free"] 
mean_apps_free = apps_free["Rating"].mean() 
print(round(mean_apps_free,2))
print("diferencia apps gratuitas y de paga:", round(mean_apps_paid/mean_apps_free,2) * 100,"%")

# 4 ¿Cuál es el 'Size' (tamaño) mínimo y máximo en la 'Category' 'COMICS'?
# Redondee la respuesta a la centésima más cercana.
print("-"*40)
print("Minimo y maximo de tamaño de aplicaciones:")
apps_comics = df[df["Category"] == "COMICS"]
comics_minmax_size = apps_comics["Size"].agg(['min', 'max'])
print(comics_minmax_size)



#Bonificación 1. ¿Cuántas aplicaciones tienen un 'Rating' de más de 4.5 en la 'Category' 'FINANCE'?
temp = df[df['Rating'] > 4.5]['Category'].value_counts()
print(temp['FINANCE'])


#Bonificación 2. ¿Cuál es la relación de juegos 'Free' y 'Paid' con un 'Rating' superior a 4.9?
temp = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print(temp['Free'] / temp['Paid'])