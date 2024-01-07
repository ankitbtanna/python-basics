# Functions - defining and declaring before is important

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

print(details)

def function_returning_multiple_values():
    return 1, 2, 3

print(function_returning_multiple_values())
print(list(function_returning_multiple_values()))


def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk("Hello World")


def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1;
        print(count)

    increment()


count()

