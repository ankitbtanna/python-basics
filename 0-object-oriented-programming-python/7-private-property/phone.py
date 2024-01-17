from item import Item

class Phone(Item):
    def __init__(self, name, price, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes/methods
        super().__init__(
            name,
            price,
            quantity
        )

        # Run validations for the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

        # Assign of property to self object
        self.broken_phones = broken_phones


phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())

print(Phone.all)