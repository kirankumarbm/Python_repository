# Reading Json file in python
import json

f = open('json_file.json','r')
data = f.read()
f.close()

# Json_Object ---> Dict
# json.lods() is opposite of json.dumps()
info = json.loads(data)
print(info)
print(info["name"]," ----------- ", info["age"])



#"json_file.json" file contains ----> {"name": "Kirankumar", "gender": "Male", "city": "Bangalore", "age": 25}

