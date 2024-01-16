from typing import List
import csv

class Item:
    pay_rate = 0.8

    all: List = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        # run validations
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"


        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_price = self.price * self.quantity

        # actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.quantity * self.price

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )


    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        # return f"Item('{self.name}', {self.price}, {self.quantity})"
        return str(vars(self))



print("######################")
Item.instantiate_from_csv()
print("######################")

print('**********************')
print(Item.is_integer(5))
print(Item.is_integer(7.5))
print(Item.is_integer(7.0))
print('**********************')


print(Item.all)

for item in Item.all:
    print(vars(item))

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)