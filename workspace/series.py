import pandas as pd


""" Crear una serie a partir de un diccionario """
serie = pd.Series([4,6,2,6,7,6,-7,6.8], index=["a","b","c","d","e","f","g","h"])

print("serie limpia:")
print(serie)
print("-"*40)

""" Metodo para retornar el valor de una serie, omitiendo los datos indicados"""
print("serie quitando a y e:")
print(serie.drop(["a","e"]))
print("-"*40)

print("serie limpia otra vez?:")
print(serie)
print("-"*40)


print("modificando valor de un indice:")
serie["a"]=64
print(serie["a"])
print("-"*40)


""" obtener series en base a una condicion """
print("menores a 4:")
print(serie[serie<4])
print("-"*40)

""" Obtener series con una condicion inversa """
print("NO menores a 4: (Mayor o igual)")
print(serie[~(serie<4)])
print("-"*40)


""" Obtener series entre un intérvalo """
print("Entre 4 y 8:")
print(serie[(4<=serie) & (serie <=8) ])
print("-"*40)
