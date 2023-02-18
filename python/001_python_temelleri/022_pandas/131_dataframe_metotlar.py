import pandas as pd

data = {
    "c1":[1,2,3,4,5],
    "c2":[10,20,30,20,50],
    "c3":["abc","bca","bcccd","asdfe","as"]
}

df = pd.DataFrame(data)
result = df["c2"].unique()
result = df["c2"].nunique()
result = df["c2"].value_counts()
result = df["c2"]**2

###############################
def kareal(x) :
    return x ** 2
###
kupal = lambda x : x ** 3  
###
result = df["c2"].apply(kupal)
###############################

result = df["c3"].apply(len)

df["c4"] = df["c3"].apply(len)

result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)

result = df.info

result = df.sort_values("c1")
result = df.sort_values("c3")
result = df.sort_values("c1",ascending=True)
result = df.sort_values("c1",ascending=False)

########################################################
data = {
    "ay":["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs", "Haziran","Nisan"],
    "kategori":["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "gelir":[20,30,15,14,32,42,12,36,52]
}
df = pd.DataFrame(data)

result = df.pivot_table(index="ay",columns="kategori",values="gelir")
#######################################################

print(result)

