import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns=["c1","c2","c3","c4","c5"])

result = df.columns
result = df.head()
result = df.head(10)
result = df.tail()
result = df.tail(10)
result = df.c2.head()
result = df["c2"].head() ## = df.c2.head()
result = df[["c2","c3"]].head()
result = df[5:15][["c2","c3"]].head()
result = df > 50
result = df[df > 50]
result = df[df["c3"] > 50]
result = df[df["c3"] > 50][["c3","c4"]]
result = df[(df["c3"] > 50) & (df["c4"] % 2 == 0)]
result = df[(df["c3"] > 50) | (df["c4"] % 2 == 0)][["c3","c4"]]
result = df.query("c3 > 50 & c4 % 2 == 0")
result = df.query("c3 > 50 | c4 % 2 == 0")[["c2","c3"]]

print(result)

