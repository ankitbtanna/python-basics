# exceptions

try:
    a = "ank"
    b = "1"
    c = a + b
except NameError:
    print("NameError")
except TypeError:
    print("TypeError")
# any other errors
except ZeroDivisionError:
    print("ZeroDivisionError")
except EOFError:
    print("EOFError")
except:
    print("except All other errors");
else:
    print("Run at the bottom of the program")
finally:
    print("End of the program")

try:
    raise Exception('An error occurred! Please try again')
except Exception as error:
    print("An error occurred! Please try again", error)


class DogNotFoundException(Exception):
    print("inside DogNotFoundException")
    pass    # use it when you are defining class without methods or a function without code

try:
    raise DogNotFoundException("DNF")
except DogNotFoundException as error:
    print("DogNotFoundException", error)

