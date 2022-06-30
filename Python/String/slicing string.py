##understanding the slicing
##
##string[start: stop-1: stepsize]
##
##
name = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(name)
print(len(name))

b = name[0:8:1]
print(b)
print(len(b))
##
c = b[0:5]
print(c)
print(len(c))

b = name[0:8]
print(b)
print(name[:10])
print(name[8::])
####
##for you understanding
##start = ?, stop = ?, stepsize = ?, blank = __
##name[start::]
##name[:stop:]
##name[start:stop]
##name[start::2]

##negative indexing for string
name = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
##
#access from name[-4] to name[-2] from left to right in name
print(name[-4:-1])

print(name[-5:-2])

##retrive the name string from first to last from right to left
print(name[-1::])
print(name[::-1])
