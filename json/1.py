# covert python to json (dict to json string)

import json

data = {
    "name" : "Aayushi",
    "score" : 95,
    "isAdmin" : False
}

json_string = json.dumps(data)     
# json.dumps = write json from a string

print(json_string)