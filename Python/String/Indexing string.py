#understanding the indexing in python

address = 'Thane west, near thane station near mcdonald'
print(len(address))
print()
print(address[0])
print()
print(address[1])
print()
print(address[-1])


add = 'Python'
print(add[0])
print(len(add))
print(add[7])

##This will give Indexerror
print(add[8])

##this wil give error, as strings are immutable
##add[0] = 'C'
add = 'Python'
##this will not get printed as we got an error above
print(add)
