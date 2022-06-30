##understanding the membership in string

full_name = input('Enter your full name: ')
sub = input('Enter the sub string to find: ')

if sub in full_name:
    print('The sub string exists: ', sub)
else:
    print('The given sub string is not available.')


full_name = input('Enter your full name: ')
sub = input('Enter the sub string to find: ')


if sub not in full_name:
    print('The sub string not exists: ', sub)
else:
    print('The given sub string is available.')
