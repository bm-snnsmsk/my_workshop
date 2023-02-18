import requests
import json

## print(requests.__file__)

result = requests.get("https://jsonplaceholder.typicode.com/todos")
##result = response = 200
## result = result.text ## string 
result = json.loads(result.text) ## python object
print(result[0]) 
print(type(result)) ## list

for i in result :
    print(i["title"])




