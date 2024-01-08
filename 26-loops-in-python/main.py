# Loops

condition = True

counter = 0;

# while loop
while condition == True:
    counter += 1
    print("Hello World!")

    if counter > 10:
        condition = False


items = [1, 2, 3, 4]

# For loop
for item in items:
    print(item)

# Using Range
for item in range(15):
    print(item)

# Range of items
for item in range(len(items)):
    print(item)

# index and item
for index, item in enumerate(items):
    print(index, item)


# Break and Continue
for item in items:
    if item == 2:
        continue
    print(item)

print("#################")

for item in items:
    if item == 2:
        break
    print(item)

