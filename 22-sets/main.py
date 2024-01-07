# Sets - no key value pairs
names = {
    "Roger",
    "Smith"
}

names_2 = {
    "Roger"
}

intersect = names & names_2
print(intersect)

union = names | names_2
print(union)

is_superset = names > names_2
print(is_superset)

is_subset = names <= names_2
print(is_subset)

difference = names - names_2
print(difference)

print(names ^ names_2)

print(list(names))
print("Smith" in list(names))

unique_set = {
    "Roger",
    "Smith",
    "Roger"
}
print(unique_set)