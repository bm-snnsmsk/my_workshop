import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("nba.csv")
#df = df.drop(["Unnamed"], axis=1).groupby("team_abbreviation").mean()
df = df.groupby("team_abbreviation").mean()

df.plot(subplots=True)
plt.legend()



plt.show()