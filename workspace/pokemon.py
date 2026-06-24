
import pandas as pd


file_path = "./dex.csv"
df = pd.read_csv(file_path)
df.info()

poke_36 = df[df["Evolve"] == "Lv. 36"]
print("Pokémons que se obtienen evolucionando al nivel 36")

print(poke_36["Pokemon"].to_string(index=False))
print("-"*40)

""" El más rápido de ellos """
print("El más rápido de ellos es:")
print(poke_36[poke_36["Spe"] == poke_36["Spe"].max()]["Pokemon"].to_string(index=False))
