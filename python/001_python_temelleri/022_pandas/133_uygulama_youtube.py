import pandas as pd

data = pd.read_csv("GBvideos.csv")

result = data.columns
result = data.head(10)
result = data[5:15].head()
result = len(data.columns)
data.drop(["thumbnail_link","comments_disabled","ratings_disabled","ratings_disabled","video_error_or_removed","description"],axis=1,inplace=True)
result = data["likes"].mean()
result = data["dislikes"].mean()
result = data.head(50)[["title","likes","dislikes"]]
result = data[data["views"] == data["views"].max()][["title","views"]]
result = data[data["views"] == data["views"].min()][["title","views"]]
result = data["views"].sort_values(ascending=False).head(10)
result = data.sort_values("views",ascending=False).head(10)[["title","views"]]
# result = data.groupby("category_id")["likes"].mean()
# result = data.groupby("category_id").mean()
# result = data.groupby("category_id").mean().sort_values("likes")["likes"]
# result = data.groupby("category_id").sum().sort_values("comment_count")["comment_count"]
# result = data["category_id"].value_counts()

data["uzunluk"] = data["title"].apply(len) 
data["tag_sayisi"] = data["tags"].apply(lambda x : len(x.split("|"))) 


def oran(dfr) :
    likesList = list(dfr["likes"])
    dislikesList = list(dfr["dislikes"])
    liste = list(zip(likesList,dislikesList))
    oranlist = [] 
    for i, j in liste : ## (likes, dislikes)
        if (i + j) == 0 :
            oranlist.append(0)
        else :
            oranlist.append(i / (i + j))
    return oranlist

    

data["oran"] = oran(data)
result = data.sort_values(["oran","likes"],ascending=False).head(50)[["title","likes","dislikes","oran"]]


print(result)
## print(data)

