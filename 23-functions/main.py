# Functions

def hello():
    print("Hello")
    return

hello()

def hello_world(name = "World"):
    print(f"Hello, {name}")

hello_world("Beau")
hello_world("Quincy")
hello_world()

def hello_person(name = "World", age = 0):
    print(f"Hello, {name}. You are {age} years old")

hello_person("Quincy")
hello_person("Quincy", 20)


# dicts are pass by reference
def hello_person_details(person):
    person["details"] = "new details"
    return person

details = {
    "details": "details"
}

hello_person_details(details)

print(details);

