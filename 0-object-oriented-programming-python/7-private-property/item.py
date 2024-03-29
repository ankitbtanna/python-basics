from typing import List
import csv

class Item:
    pay_rate = 0.8

    all: List = []


    # Private attribute - self.__name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __init__(self, name: str, price: float, quantity: int = 0):
        # run validations
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"


        # assign to self object
        self._name = name
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
        print(self.__class__.__name__)
        # return f"Item('{self.name}', {self.price}, {self.quantity})"
        return str(vars(self))

