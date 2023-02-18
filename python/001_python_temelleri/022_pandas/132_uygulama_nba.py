import pandas as pd

data = pd.read_csv("nba.csv")

# result = data.columns
# result = len(data.columns)
# result = data.head()
# result = data.head(10) 
# result = len(data.index) ## topplam kayıt
# result = data["age"].max() ## max yaş

result = data["age"].mean() ## yaş ortalaması
result = data["age"].sum() / len(data.index) ## yaş ortalaması
result = data[data["age"] == data["age"].max()]["player_name"] 
result = data[data["age"] == data["age"].max()]["player_name"].iloc[0] ## sadece isim bilgisi
result = data.query("age > 20 & age < 24")[["player_name","team_abbreviation","age"]].sort_values("age",ascending=False)
result = data.query("player_name == 'John Holland'")[["team_abbreviation","player_name"]]
result = data.groupby("team_abbreviation")["age"].mean().sort_values()
result = len(data.groupby("team_abbreviation").count()) ## toplam takım sayısı
result = len(data.groupby("team_abbreviation")) ## toplam takım sayısı
result = data["team_abbreviation"].nunique() ## toplam takım sayısı
result = data["team_abbreviation"].unique() ## tekrarsız takımlar
result = data.groupby("team_abbreviation")["player_name"].count().sort_values() ## herbir takımın oyuncu adedi
result = data["team_abbreviation"].value_counts().sort_values() ## her bir takımın oyuncu adedi
result = data[data["player_name"].str.contains("and")][["player_name","team_abbreviation"]]



print(result)

