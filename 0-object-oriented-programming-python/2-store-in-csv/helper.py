# when to use class method or static method

class Item:
    @staticmethod
    def is_integer():
        """
        do something that is not unique to the instance but is related to the class
        return True or False
        """
        return True

    @classmethod
    def instantiate_from_csv(cls):
        """
        This should also do something that has a relationship with the class
        but usually these are used to manipulate
        different structures of data to instantiate object
        """
        return True


# Static methods don't pass the object reference as the first argument
# Class methods pass class reference as the first argument
# Never call static or class method from instantiated object. Always call them from Class.
