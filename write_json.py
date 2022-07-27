# writing into Json file in python
import json

# Dictionary
user = {
    "name": "Kirankumar",
    "gender":"Male",
    "city":"Bangalore",
    "age": 25
}
# converting Dict --> Json_object.
data = json.dumps(user)

f = open('json_file.json','w')
f.write(data)
f.close()


#"json_file.json" file contains ----> {"name": "Kirankumar", "gender": "Male", "city": "Bangalore", "age": 25}
