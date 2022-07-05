# To read a file using python script, the python provides
# to read() method.

# open a file with 'r' mode
with open('C:\Pythonfullstack\Python\Akbar_birbal.txt', 'rb') as f:
    content = f.read()
    print(content)
    print(type(content))


# open file with 'r' mode


with open('C:\Pythonfullstack\Python\Akbar_birbal.txt', 'rb') as f:
    content = f.read()
    print(content)
    print()
    print(type(content))

