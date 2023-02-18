import pandas
import numpy as np

arr = [20,30,40,50,60]  # numbers
arr = ["20","30","40","50","60"] # object
arr = [20,"30",40,"50","60"]  # object
arr = 5 
dict = {'a':5,'b':10,'c':15,'d':20} 
arr = np.array([20,30,50,60,70,80])
arr = np.random.randint(10,100,6)


pandas_series = pandas.Series(arr)
pandas_series = pandas.Series(5, [0,1,2,4])
pandas_series = pandas.Series(5, ['a','b','c','d'])
pandas_series = pandas.Series(dict)
pandas_series = pandas.Series(arr)
pandas_series = pandas.Series(arr)[0]
pandas_series = pandas.Series(arr)[-2:]


print(pandas_series)