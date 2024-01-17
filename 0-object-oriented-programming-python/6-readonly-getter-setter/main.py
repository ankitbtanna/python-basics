from item import Item
from phone import Phone

Item.instantiate_from_csv()

item1 = Item("MyItem", 750)

# print(item1.read_only_name)

try:
    item1._name = "New Item"
    # item1.read_only_name = "New AAA"
except AttributeError as error:
    print("came here")
    print(f"This is the error: {error}")

    # print(item1.read_only_name)

print(item1.name)