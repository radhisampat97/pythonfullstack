# The 'with' statement is useful in the case of manipulating the files'

#with open(filename, accessmode) as filepointer


with open('C:\Pythonfullstack\Python\Akbar_birbal.txt', 'rb') as f:
    content = f.read()
    print(content)
