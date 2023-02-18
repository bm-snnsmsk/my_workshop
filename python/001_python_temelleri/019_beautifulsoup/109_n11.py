import requests
from bs4 import BeautifulSoup

###### kodlar çalışmadı 
##############################
url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("li",{"class":"column"})
print(html)

for i in list :
    name = i.div.a.h3.text.strip()
    link = i.div.a.get("href")
    oldprice = i.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
    newprice = i.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip("TL")
    print(f"{name} - {link} - {oldprice} - {newprice}")