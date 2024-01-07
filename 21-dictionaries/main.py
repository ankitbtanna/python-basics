# Dictionaries - Objects, key value pairs
dog = {
    "name": "Roger",
    "age":  8,
    "vaccinated": True
}

print(dog["name"])

dog["name"] = "Sid"

print(dog)

print(dog.get("name"))
print(dog.get("color"))
print(dog.get("color", "Brown")) # default value

dog["color"] = "Green"
print(dog.get("color"))

print(dog.pop("name"))
print(dog)

print(dog.popitem()) # removes last item added to dictionary
print(dog)

print("color" in dog)

print(dog.keys())
print(list(dog.keys()))

print(dog.values())
print(list(dog.values()))

print(dog.items())
print(list(dog.items()))

print(len(dog))

dog["food"] = "meat"
dog["standing height"] = 5

print(dog)

del dog["standing height"]
print(dog)

print(dog.copy())
