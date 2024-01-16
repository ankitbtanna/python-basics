class Item:
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity: int = 0):
        # run validations
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"


        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        self.total_price = self.price * self.quantity

    def calculate_total_price(self):
        return self.quantity * self.price


item1 = Item("Phone", 100, 5)

print(item1)
print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.calculate_total_price())

print("########")

item2 = Item("Laptop", 1000, 3)

print(item1)
print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.calculate_total_price())

print(item2.calculate_total_price())


item3 = Item("Tablet", 800, 2)
print(item3.name)
print(item3.price)
print(item3.quantity)
print(item3.calculate_total_price())

item3 = Item("Watch", 500, 3)

item2.pay_rate = 10

# Class attribute vs Instance attribute
print(f"This is a Class Attribute for class {Item.pay_rate}")
print(f"This is a Instance Attribute for item1 {item1.pay_rate}")
print(f"This is a Instance Attribute for item2 {item2.pay_rate}")

# Dictionary - to see all the attributes of the object:
print(f"All the attributes for Class {Item.__dict__}")
print(f"All the attributes for instance {item1.__dict__}")

# Methods starting and ending with __METHODNAME__ are called magic methods

# # store management system - Tracking items in our store
# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity
#
#
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(item1_price_total))
# print(type(item1_price_total))
#
# # Class - data type of our own, attributes and methods
#

# instance attributes are specific to the instances
# Class attributes are common for all the instances - static?

