import pandas as pd
import numpy as np

s1 = pd.Series([3,4,1,5,100])
s2 = pd.Series([13,14,11,15])
data = {"apple":s1,"oranges":s2}
data = dict(apple=s1,oranges=s2) ## = data = {"apple":s1,"oranges":s2}
df =  pd.DataFrame(data)


data = [["sinan",70],["baran",96],["emine",89],["tuba",78]]
df = pd.DataFrame(data, index = [1,2,3,4], columns=["isim","derece"])


data = {
    "name":["sinan","baran","tuba","emine"],
    "grade":[56,87,95,45]
    }
df = pd.DataFrame(data,index=["212","312","412","512"])


data = [
    {"name":"tuba","grade":78},
    {"name":"baran","grade":89},
    {"name":"emine","grade":67},
    {"name":"sinan","grade":98}
    ]
df = pd.DataFrame(data,index=["212","312","412","512"])


print(df)

