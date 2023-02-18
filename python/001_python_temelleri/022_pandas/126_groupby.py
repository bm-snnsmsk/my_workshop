import pandas as pd
import numpy as np

personeller = {
    "calisanlar":["sinan","baran","emine","tubanur","rizgar","kendal","nujin"],
    "departman":["insan kaynakları","bilgi işlem","muhasebe","insan kaynakları","bilgi işlem","muhasebe","bilgi işlem"],
    "yaş":[30,25,42,45,50,23,39],
    "semt":["kadıköy","tuzla","maltepe","tuzla","kadıköy","tuzla","maltepe"],
    "maaş":[3000,3000,4000,3500,2750,6500,4500]
}
df = pd.DataFrame(personeller)

result = df["maaş"].sum()

result = df.groupby("departman") ## object ile ilgili bilgiler
result = df.groupby("departman").groups
result = df.groupby(["departman","semt"]).groups

# for name, group in df.groupby("departman") :
#     print(name)
#     print(group)

result = df.groupby("semt").get_group("kadıköy")
result = df.groupby("departman").get_group("muhasebe")

# result = df.groupby("departman").sum() ## ileri bir versiyonda kaldırılacakmış
# result = df.groupby("departman").mean() ## ileri bir versiyonda kaldırılacakmış

result = df.groupby("departman")["maaş"].mean() 
result = df.groupby("semt")["maaş"].mean() 
result = df.groupby("semt")["maaş"].count() 
result = df.groupby("semt")["maaş"].max()
result = df.groupby("semt")["maaş"].max()["kadıköy"]

# result = df.groupby("departman").agg(np.mean) ## ileri bir versiyonda kaldırılacakmış
result = df.groupby("departman")["maaş"].agg(np.sum) 
result = df.groupby("departman")["maaş"].agg([np.sum, np.mean, np.max, np.min])
result = df.groupby("departman")["maaş"].agg([np.sum, np.mean, np.max, np.min]).loc["muhasebe"]




print(result)

