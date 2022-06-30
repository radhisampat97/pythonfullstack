##understanding the startwith and endswith
##
##main_string.startswith(sub_string)

name = input('Enter your name: ')
substring = input('Enter the substring: ')
##n = name.startswith(substring)
##print(n)

if name.startswith(substring):
    print('yes')
else:
    print('no')


#understanding the endswith
##main_string.endswith(sub_string)

name = input('Enter your name: ')
substring2 = input('Enter the substring: ')

if name.endswith(substring2):
    print('yes')
else:
    print('no')

