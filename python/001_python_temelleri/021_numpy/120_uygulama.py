import numpy as np

result = np.array([10,15,30,45,60])
result = np.arange(5,15)
result = np.arange(50,100, 5)
result = np.zeros(10)
result = np.ones(10)
result = np.linspace(0,100,5)
result = np.random.randint(10,30,5)
result = np.random.randn(5)
result = np.random.randint(10,50,15).reshape(3,5)
result = np.random.randint(10,50,15).reshape(3,5).sum(axis=1) ## satır toplamı 
result = np.random.randint(10,50,15).reshape(3,5).sum(axis=0) ## sutun toplamı
result = np.random.randint(10,50,15).reshape(3,5).max()
result = np.random.randint(10,50,15).reshape(3,5).min()
result = np.random.randint(10,50,15).reshape(3,5).mean()
result = np.random.randint(10,50,15).reshape(3,5).argmax()
result = np.random.randint(10,50,15).reshape(3,5).argmin()
result = np.arange(10,20)[:3]
result = np.arange(10,20)[::-1]
result = np.random.randint(10,50,15).reshape(3,5)[:1]
result = np.random.randint(10,50,15).reshape(3,5)[2,3]
result = np.random.randint(10,50,15).reshape(3,5)[:,:0] ## tüm satırların ilk elemanı
result = np.random.randint(10,50,15).reshape(3,5)**2 # tüm elemanların karesi
matris = np.random.randint(-50,50,15).reshape(3,5)
ciftler = matris[matris % 2 == 0]
result = ciftler[ciftler > 0]




print(result)