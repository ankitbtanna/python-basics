from item import Item

Item.instantiate_from_csv()

item1 = Item("MyItem", 750)

item1.__name
print(item1.__name)