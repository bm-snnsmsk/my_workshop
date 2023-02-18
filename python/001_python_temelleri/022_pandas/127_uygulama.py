import pandas as pd
import numpy as np

df = pd.read_csv("imdb_top250.csv")

result = df.info
result = df.head()
result = df.head(10)
result = df.tail()
result = df.tail(10)
result = df["Title"].head()
result = df[["Title","imdbRating"]].head()
result = df[["Title","imdbRating"]].tail(7)
result = df[5:][["Title","imdbRating"]].head()
result = df[df["imdbRating"] > 8.0][["Title","imdbRating"]].head(50)
result = df.columns
result = df.query("Year >= 2014 & Year <= 2015")["Title"]




print(result)

