import numpy as np
 


n1 = np.random.randint(10,100,6)
n2 = np.random.randint(10,100,6)

result = n1 + n2 
result = n1 + 10
result = n1 - n2 
result = n1 - 10
result = n1 * n2
result = n1 * 10
result = n1 / n2
result = n1 / 10

result = np.sin(n1)
result = np.cos(n1)
result = np.log(n1)
result = np.sqrt(n1)

mtn1 = n1.reshape(2,3)
mtn2 = n2.reshape(2,3)

result = np.vstack((mtn1,mtn2))
result = np.hstack((mtn1,mtn2))

result = n1 >= 50
result = n1[n1>=50]


# print(n1)
# print(n2)
print(result)

