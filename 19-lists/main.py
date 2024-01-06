my_list = ["Roger", 1, True, {}]

print(len(my_list))

print("Roger" in my_list)
print("Beau" in my_list)

print(my_list[0])
print(my_list[:2])
print(my_list[1:])

my_list[2] = False

print(my_list)
print(my_list[-1])

my_list.append("Fred")
print(my_list)

my_list.pop()
print(my_list)

my_list += ["new item"]
print(my_list)

my_list.remove("new item")
print(my_list)