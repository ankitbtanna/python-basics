numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# simpler
numbers_power_2 = [num**2 for num in numbers]
print(numbers_power_2)

# more lines
num_powers_2_new = []
for num in numbers:
    num_powers_2_new.append(num**2)
print(num_powers_2_new)

numbers_power_2_using_map = list(map(lambda x: x**2, numbers))
print(numbers_power_2_using_map)
