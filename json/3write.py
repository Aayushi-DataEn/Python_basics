import json

data = {
    "name" : "Aayushi",
    "score" : 95,
    "isAdmin" : False
}

with open ('data.json', 'w') as file:
    json.dump(data, file, indent= 4)
    # json.dump = write json from a file