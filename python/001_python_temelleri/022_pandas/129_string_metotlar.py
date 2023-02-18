import pandas as pd
import numpy as np


data = pd.read_csv("sample.csv")
#data = data.dropna()
# data = data.dropna(inplace=True)
# data = data.columns

# data = data["Host"].str.upper()
# data = data["Host"].str.lower()
# data["index"] = data["Host"].str.find("a")
# data["index"] = data["Host"].str.contains("a")
# data["index"] = data.Host.str.contains("a")
# data = data[data.Host.str.contains("a")][["Host","index"]]
# data = data.Host.str.replace("a","A")
# data = data.Host.str.replace("a","A").replace("e","E")
data = data.Host.loc[data["Host"].str.split("a").str.len()==2].str.split(expand=True)




print(data.head(10))

