done = True
not_done = False

# Capital T or Capital F

if done:
    print("yes")
else:
    print("no")

if not done:
    print("no")
else:
    print("yes")


non_boolean = -1

if non_boolean:
    print("done")
else:
    print("not note")

print(type(done) == bool)

book1 = True
book2 = False

read_any_book = any([book1, book2]);
print(read_any_book)

read_all_books = all([book1, book2]);
print(read_all_books)