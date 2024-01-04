a = [1, 2, 3]
b = a
print(b is a)
print(a is b)
print(a is not b)

print('##################')

c = [4, 5, 6]
d = [4, 5, 6]
print(c is d)
print(d is c)
print(c is not d)

print('##################')

my_list = [1, 2, 3]
print(3 in my_list)
print(4 in my_list)

my_dictionary = { "a": 1, "b": 2, "c": 3 }
print('b' in my_dictionary)