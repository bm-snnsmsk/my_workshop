import numpy as np
 

numbers1 = np.array([0,5,10,15,20,25])

result = numbers1[2]
result = numbers1[-2]
result = numbers1[-1]
result = numbers1[0:2]
result = numbers1[:2]
result = numbers1[2:]
result = numbers1[::]
result = numbers1[::2]
result = numbers1[::-1]
result = numbers1[::-2]

arr1 = np.array([[0,5,10],[15,20,25],[30,35,40]])
result = arr1[0]
result = arr1[0,2]
result = arr1[2,2]
result = arr1[:,2]
result = arr1[:,0:2]
result = arr1[-1,:]
result = arr1[:3,:3] 
result = arr1[:2,:2] 



print(result)