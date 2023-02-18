import json

person = '{"name":"sinan", "languages" :["python", "C#"]}'

result = json.loads(person)
result = result["languages"]

print(result)


with open("person.json") as f :
    data = json.load(f)
    print(data)

person_dict = {
    "name":"ali",
    "languages":["python", "C#"]
}

sonuc = json.dumps(person_dict)
print(sonuc)


with open("person2.json","w") as f :
    json.dump(person_dict,f)

son = json.dumps(person_dict, indent= 4)
print(son)   