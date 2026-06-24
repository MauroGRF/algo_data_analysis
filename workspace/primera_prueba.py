import pandas as pd
import rich


diccionario= [
    {"a":2, "b":4, "c":6},
    {"a":3, "b":6, "c":4},
    {"a":5, "b":9, "c":9},
]

df = pd.DataFrame(diccionario)

print(df)
