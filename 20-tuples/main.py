# Tuples - fundamental data structure in python
# Immutable group of objects, once tuple is created it cannot be modified

names = ("Roger", "Smith")
print(names)

print(names[0])
print(names[1])
print(names[-1])

print(names.index("Smith"))

print(len(names))

print("Roger" in names)
print(names[0:2])

new_names = ("Roger", "Smith", "Beu")
print(sorted(new_names))

new_names_tuple = new_names + ("Amanda", "Berdie")
print(new_names_tuple)