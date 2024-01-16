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

print(f"This is a Class Attribute {Item.pay_rate}")

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

