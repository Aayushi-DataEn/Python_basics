# convert json to python (json string to dict)

import json

json_data = '{"name": "Aayushi", "score": 95, "isAdmin": false}'

data_dict = json.loads(json_data)
# json.loads = reads json from a string
print(data_dict)