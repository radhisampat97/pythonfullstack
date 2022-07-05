# Python provides open() function that accepts two arguments
## filename and access mode in which that file is accessed

# file_obj = open(fileName, accessMode)

# opens the file akbar_birbal.txt in read mode

file_obj = open(r'C:\Pythonfullstack\Python\Akbar_birbal.txt', 'r')
print(dir(file_obj))
print(file_obj)
print('file opened successfully')

file_obj.close()

# open file with 'r' mode
with open (
