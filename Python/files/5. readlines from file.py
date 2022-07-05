# Python provides the 'readlines()' method, it is used for reading lines

## open a file with 'r' mode
##with open('C:\Pythonfullstack\Python\Akbar_birbal.txt', 'rb') as f:
##    content = f.readlines()
##    print(content)


### file pointer position
##with open('C:\Pythonfullstack\Python\Akbar_birbal.txt', 'rb') as f:
##    print('The file pointer is at: ', f.tell())
##    content = f.read(50)
##    print(content)
##    print('The file pointer is at: ', f.tell())

## Set the pointer location
# fileobj.seed(offset, from)
# offset: it refers to the noew position of the pointer
# from: it indicates the reference position from where the bytes are to be moved
# from = 0: it referes the beginning of the file
# from = 1: the current position
# from = 2: the end of the pointer is used to reference
with open('C:\Pythonfullstack\Python\Akbar_birbal.txt', 'rb') as f:
    print('The file pointer is at: ', f.tell())
    f.seek(10)
    print('The file pointer is at: ', f.tell())
    content = f.read(20)
    print('The file pointer is at: ', f.tell())
    print(content)


    

