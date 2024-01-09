# Class

class Dog:
    def __init__(self):
        print("Dog class")

    def bark(self):
        print("woof")


dog = Dog()

print(type(dog))
dog.bark()


class Activity:
    @staticmethod
    def walk():
        print("Walking...")

class Job:
    def job(self):
        print("Job class")



class Person(Activity, Job):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name}, I am {self.age} years old")


person = Person("John", "23")
person.introduce()
person.walk()
person.job()
