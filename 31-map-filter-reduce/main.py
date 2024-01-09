# Map, Filter, Reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def double(a):
    return a * 2

result = map(double, numbers)
print(list(result))


double_2 = lambda num: num * 2

result_2 = map(double_2, numbers)
print(list(result_2))


result_3 = map(lambda a: a * 2, numbers)
print(list(result_3))


is_even = lambda num: num % 2 == 0
result = filter(is_even, numbers)
print(list(result))


expenses = [
    ('Dinner', 80),
    ('Car Repair', 120)
]


total_expenses = 0

for expense in expenses:
    total_expenses += expense[1]

print(total_expenses)


from functools import reduce

tip = 10
all_expenses = reduce(lambda a, b: a + b[1], expenses, tip)
print(all_expenses)
