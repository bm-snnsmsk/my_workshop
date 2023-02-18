import requests

class Github :
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "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"

    def getUser(self, username) :
        response = requests.get(self.api_url+"/users/"+username)
        return response.json() ## alternatif json.loads(response)
    def getRepositories(self, username) :
        response = requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json() ## alternatif json.loads(response)
    def createRepository(self,name) :
        response = requests.post(self.api_url+"/user/repos?access_token="+self.token, json = {
            "name":"sinan",
            "description":"this is your first repository",
            "homepage":"https://github.com",
            "private":False,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True
        })
        return response.json() ## alternatif json.loads(response)
        pass

github = Github()
while True :
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSecim : ")
    if secim == "1" :
        username = input("username : ")
        result = github.getUser(username)
        print(f"name : {result['name']}, public repos : {result['public_repos']}, takipçi : {result['followers']}")
    elif secim == "2" :
        username = input("username : ")
        result = github.getRepositories(username)
        ## print(result[0]["name"])
        for i in result :
            print(i['name'])
    elif secim == "3" :
        name = input("name : ")
        result = github.createRepository(name)
        print(result)
        pass
    elif secim == "4" :
        break
    else : 
        print("Yanlış Seçim : ")

