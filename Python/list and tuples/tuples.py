##to create tuples

tup1 = (10,)
tup1 = ('Anurag',)

print(tup1)
print(type(tup1))

tup3 = 1,2,3,4,5,6
tup3 = 'Anurag', 'Shristi', 'Aman'
print(tup3)
print(type(tup3))


lst = [10,20,30]
print(lst)
print(type(lst))
tupL = tuple(lst)
print(type(tupL))
print(tupL)

##indexing and slicing for tuples

tup = (10,20,30,40,50,60,70,80,90,'Anurag', 'Python', 'HTML')
print(tup[9])
print(tup[9:])
print(tup[-1])

## basic functions for tuple
tup = (90,80,70,60,50,40,30,20,10)
print(len(tup))
print(min(tup))
print(max(tup))
print(tup.count(90))
print(tup.index(90))
print(sorted(tup))

## nested tuple
tup = (50,60,74,85,94,785,625,487,523, (168,6154,6,85426,654,5246,(64,917,7891)))

print(tup)
