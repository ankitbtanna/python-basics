# This is a comment, it gets ignored

str_variable = '%%%'

print(type(str_variable))
print(type(str_variable) == str)
print(isinstance(str_variable, str))
print(str_variable);

is_male = True
print(type(is_male))

age = 2
print(type(age))

height = 1.8
print(type(height))

print(type({"name": "Abc"}))

float_age = float(age)
string_age = str(float_age)

print(type(float_age))
print(type(string_age))

number_age = "20"
age_from_number = int(number_age)