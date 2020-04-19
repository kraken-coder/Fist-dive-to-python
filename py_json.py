import json

#  sample json 

useJSON = '{ "first_name": "john", "age": 20}'

user = json.loads(useJSON)
print(type(user))


# dict to json

car = {"make": "ford", "model": "mustang"}
carJSON = json.dumps(car)
print(carJSON)