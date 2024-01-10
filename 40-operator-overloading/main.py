class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        # return True if self.age > other.age else False
        return self.age > other.age

roger = Dog("Robert", 5)
syd = Dog("Sydney", 3)

print(roger > syd)
