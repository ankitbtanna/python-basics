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

my_list.insert(2, "new item at 2")
print(my_list)

# insert multiple items in the list
my_list[1:1] = ["Test 1", "Test 2", "Test 3"]
print(my_list)

my_list_nums = [1, 2, 5, 3, 8, 0]
print(my_list_nums.sort())
print(my_list_nums)

# sorted() global function does not modify existing array, it returns a new array
my_list_names = ["Roger", "Beau", "Andy", "Charlie", "beckie", "Karl"]
sorted_list_names = sorted(my_list_names, key=str.lower)
print(sorted_list_names)
print(my_list_names)

copy_my_list = my_list.copy()
print(copy_my_list)

