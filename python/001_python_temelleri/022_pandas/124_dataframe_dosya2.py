import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index=["a","b","c"],columns=["column1","column2","column3"])

result = df["column1"]
result = df[["column1","column2"]]
result = df.loc["a"]

result = df.loc[:,"column1"]
result = df.loc[:,["column1","column2"]]
result = df.loc[:,"column1":"column3"]
result = df.loc[:,:"column3"]
result = df.loc["a":"c",:"column2"]
result = df.loc["a":"b","column2"]
result = df.loc[:"b","column2"]
result = df.iloc[2]
result = df.loc[:,"column2"]
result = df.loc["a","column2"]
result = df.loc[["a","b"],["column2","column3"]]

## sütün ekleme ekleme
df["column4"] = pd.Series(randn(3), ["a","b","c"])
df["column5"] = df["column2"] + df["column3"]

result = df.drop("column4",axis=1,inplace=True)  # axis=1 y ekseni



print(df)
print(result)

