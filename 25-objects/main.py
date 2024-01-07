# Object

age = 10

print(age.real)
print(age.imag)
print(age.bit_length()) # number of bits necessary for representing this number in binary

items = [1, 2]
print(items.append(3))
items.pop()

print(id(items)) # location of memory of the items

# age = age + 1 is a new object as compared to age = 10, hence age is immutable
# if the object provides methods for mutation, then it is mutable else it is immutable