from item import Item

Item.instantiate_from_csv()

item1 = Item("MyItem", 750)

print(item1.name)

print(item1.price)

item1.increment_price(0.2)

print(item1.price)

item1.apply_discount()

print(item1.price)