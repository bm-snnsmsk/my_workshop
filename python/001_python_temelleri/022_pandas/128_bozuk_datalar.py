import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data, index= ["a","c","e","f","h"],columns=["c1","c2","c3"])
df = df.reindex(["a","b","c","d","e","f","g","h"])

# result = df.drop("c1",axis=1)
# result = df.drop(["c1","c3"],axis=1)
# result = df.drop("c",axis=0)
# result = df.drop(["a","c","d"],axis=0)

result = df.isnull()
result = df.notnull()
result = df.notnull().sum()
result = df.isnull().sum()
result = df["c1"].isnull().sum()
result = df["c1"].isnull()

newColumn = [np.nan,30,np.nan,np.nan,40,45,19,np.nan]
df["c4"] = newColumn

result = df[df["c1"].isnull()]
result = df[df["c1"].isnull()]["c1"]
result = df[df["c1"].notnull()]
result = df[df["c1"].notnull()]["c1"]

result = df.dropna() ## = result = df.dropna(axis=0) ## row
result = df.dropna(axis=1) ## coloumn
result = df.dropna(how="any") ## en az bir NaN varsa sil, geri kalanları getir
result = df.dropna(how="all") ## tümü NaN ise sil, geri kalanları getir
result = df.dropna(subset=["c1","c2"],how="all") 
result = df.dropna(subset=["c1","c2"],how="any") 
result = df.dropna(thresh=2) 
result = df.dropna(thresh=3) 
result = df.dropna(thresh=1) 

result = df.fillna(value="no input") 
result = df.fillna(value=1) 

result = df.sum()
result = df.sum().sum() 
result = df.size
result = df.isnull().sum()
result = df.isnull().sum().sum()
result = df.notnull().sum()
result = df.notnull().sum().sum()

################################
def ortalama(df) :
    toplam = df.sum().sum()     
    hucre = df.size - df.isnull().sum().sum()
    return toplam / hucre

result = df.fillna(value=ortalama(df))
###############################


print(result)

