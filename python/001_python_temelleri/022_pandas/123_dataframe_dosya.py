import pandas as pd
import numpy as np


df = pd.read_csv("sample.csv")
df = pd.read_excel("sample.xlsx", encoding="UTF-8") ## pip install xlrd yüklenmeli
df = pd.read_json("sample.json", encoding="UTF-8")



print(df)

