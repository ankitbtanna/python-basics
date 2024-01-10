""" Dog Module

This is a Dog Module that has a class Dog. It does bla bla bla...

- dog
- bark
"""


class Dog:
    """A class representing dog"""
    def __init__(self, name, breed):
        """Initializing a new dog"""
        self.name = name
        self.breed = breed

    def bark(self):
        """Let the dog bark"""
        print('I am barking!')


print(help(Dog))

