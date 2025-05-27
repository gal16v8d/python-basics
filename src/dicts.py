# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
mydict = {"name": "Ares", "age": 12}
# type
print(type(mydict))
# value
print(mydict)
# size
print(len(mydict))
# get some value in dict
print(mydict["name"])
# using get avoid exception if key is not present returning None instead
print(mydict.get("name"))
# check if key is present
print("name" in mydict)

# More operations
person = {
    "name": "Camilo",
    "last_name": "Rico",
    "langs": ["python", "javascript"],
    "age": 99,
}
person["name"] = "santi"
person["age"] -= 10
person["langs"].append("java")
print(person)

del person["last_name"]
person.pop("age")
print(person)
# list of key and values as tuples
print("items =>", person.items())
# just list of keys
print("keys =>", person.keys())
# just list of values
print("values =>", person.values())
