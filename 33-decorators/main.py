# Decorators - change enhance or alter how a function works
import time


def logtime(func):
    def wrapper():
        print("Before calling " + str(time.time_ns()))
        val = func()
        print("After calling " + str(time.time_ns()))
        return val
    return wrapper;



@logtime
def sayHello():
    print("Hello")

sayHello()
