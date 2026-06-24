import pandas as pd


df = pd.read_csv("cristiano_youtube_stats.csv")

df.info()

first_5 = df.head()

first_5.to_csv("siu.csv")

