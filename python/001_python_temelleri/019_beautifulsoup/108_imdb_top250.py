import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
list = soup.find("tbody",{"class":"lister-list"}).find_all("tr", limit = 10)
counter = 0 
for i in list :
    counter += 1
    filmName = i.find("td", {"class":"titleColumn"}).find("a").text
    filmYear = i.find("td", {"class":"titleColumn"}).find("span").text.strip("()")
    filmRating = i.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text
    print(str(counter).rjust(3," ")+" - "+filmRating+" - "+filmYear+" - "+filmName)