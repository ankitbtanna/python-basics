file_name = './abc.txt'

# neads closing of file to be done manually
try:
    file = open(file_name, 'r')
    content = file.read()
    print(content)
finally:
    file.close()


# Automatically closes the file
with open(file_name, 'r') as file:
    content = file.read()
    print(content)
