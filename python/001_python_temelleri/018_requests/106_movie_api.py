import requests

class theMovieDb :
    def __init__(self) :
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "0cd3b625da34a8cedab76dcee994505d"
    
    def getPopulars(self) :
        response = requests.get(f'{self.api_url}"/movie/popular?api_key={self.api_key}&language=en-US&page=1"')
        return response.json()
    def getsearchResults(self, keyword) :
        response = requests.get(f'{self.api_url}"/search/keyword?api_key={self.api_key}&query={keyword}&page=1"')
        return response.json()

movieApi = theMovieDb() 
while True :
    secim = input("1- Popular Movies\n2- Search Movie\n3- Exit\nSeçim : ")
    if secim == "1" :
        result = movieApi.getPopulars()
        for i in result['results'] :
            print(i['title']) 
    elif secim == "2" :
        aranan = input("aramak istediğiniz film adını girin : ")
        result = movieApi.getsearchResults(aranan)
        for i in result['results'] :
            print(i['name'])  
    elif secim == "3" :
        pass
    else :
        print("yanlış seçim")

 