# A collection is a collection:  which is unordered, changable and indexed

# create a dictionary
person = {
    "first_name": "john",
    "last_name": "Doe",
    "age" : 30
}
# creat using a dictionary
# person2 = dict({"frist_name" : "jj"})

# get a value of a dictionary
# print(person["first_name"])
# print(person.get("last_name"))

# add to a dictionary
# person["phone"] = "555-55-5555"

# get  keys
# print(person.keys())

#  get items
# print(person.items())

#  get values
# print(person.values())

#  duplicate 
# person2 = person.copy()
# person2["city"] = "niamey"
#  remove an item
# del(person["age"])
# person.pop("first_name")


#  clear out a dictionary
# person.clear()

#  get length
# print(len(person))


#  list of dictionary
people = [
    {"name": 'marga', "age": 20},
    {"name": 'kevin', "age": 30},
    {"name": 'ibrahima', "age": 40}
]
print(people[0]["name"])
print( person)