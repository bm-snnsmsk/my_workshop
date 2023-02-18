import numpy as np
 
# python list 
py_list = [1,2,3,4,5,6,7,8,9]

#numpy array 
np_arr = np.array(py_list)
np_multi = np_arr.reshape(3,3)

result = np_arr.ndim
result = np_multi.ndim
result = np_arr.shape
result = np_multi.shape

result = np.arange(2,16)
result = np.arange(2,16, 3)

result = np.zeros(10)
result = np.ones(10)

result = np.linspace(10, 100, 5) ## 0-100 arasını 5 e böler

result = np.random.randint(0,20)
result = np.random.randint(20)
result = np.random.randint(20, 50, 5)
result = np.random.rand(5)
result = np.random.randn(5)

result = np_multi.sum()
result = np_multi.sum(axis=0)
result = np_multi.sum(axis=1)

result = np_multi.max()
result = np.random.randint(5,25,5).max()
result = np_multi.min()
result = np.random.randint(5,25,5).min()

result = np_multi.mean()
result = np.random.randint(5,25,5).mean()

result = np_multi.argmax()
result = np.random.randint(5,25,5).argmax()

result = np_multi.argmin()
result = np.random.randint(5,25,5).argmin()










# print(type(np_arr))
# print(np_multi)
# print(np_arr.shape)
# print(np_multi.shape)

print(result)