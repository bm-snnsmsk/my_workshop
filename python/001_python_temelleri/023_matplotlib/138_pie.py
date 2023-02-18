import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


goal_types = "penalti","serbest vuruş","köşe vuruşundan atılan gol"
goals = [12,35,7]
colors = ["y","r","b"]
## plt.pie(goals,labels=goal_types,colors=colors)
plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.01,0.01,0.25),autopct="%1.1f%%")

plt.show()