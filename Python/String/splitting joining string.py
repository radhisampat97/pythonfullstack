##understanding to split and join string

## main_string.split(pattern)

main_string = 'one, two three,four@Five$Six'
sub_string = main_string.split('@')
print(sub_string)

main_string2 = 'one two three four'
sub_string2 = main_string2.split()
print(sub_string2)

#.split() means spliting based on spaces in the input
list_colours = input('Enter colours with spaces:  ').split()
print(list_colours)
###joining of the string
###  separator.join(string)

joined_string = '...'.join(list_colours)
print(joined_string)
