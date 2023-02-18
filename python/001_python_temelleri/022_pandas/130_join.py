import pandas as pd
import numpy as np

customers = {
    "CustomerId": [1,2,3,4],
    "FirstName": ["Sinan","Baran","Emine","Tubnur"],
    "LastName": ["şimşek","pelçim","rizgar","sosın"]
}
orders = {
    "OrderId": [103,204,306,408],
    "CustomerId": [1,2,5,7],
    "OrderDate": ["2010-07-04","2019-02-02","2022-04-12","2022-10-10"]
}

df_customers = pd.DataFrame(customers, columns=["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders, columns=["OrderId","CustomerId","OrderDate"])

print(df_customers)
print(df_orders)


result = pd.merge(df_customers,df_orders,how="inner")
result = pd.merge(df_customers,df_orders,how="left")
result = pd.merge(df_customers,df_orders,how="right")
result = pd.merge(df_customers,df_orders,how="outer")


#####################################

customerA = {
    "CustomerId": [1,2,3,4],
    "FirstName": ["Sinan","Baran","Emine","Tubnur"],
    "LastName": ["şimşek","pelçim","rizgar","sosın"]
}

customerB = {
    "CustomerId": [1,2,3,4],
    "FirstName": ["Sinan","Baran","Emine","Tubnur"],
    "LastName": ["şimşek","pelçim","rizgar","sosın"]
}

df_customerA = pd.DataFrame(customerA, columns=["CustomerId","FirstName","LastName"])
df_customerB = pd.DataFrame(customerB, columns=["CustomerId","FirstName","LastName"])


result = pd.concat([df_customerA,df_customerB])
result = pd.concat([df_customerA,df_customerB],axis=1)
result = pd.concat([df_customerA,df_customerB],axis=0)



print(result)

