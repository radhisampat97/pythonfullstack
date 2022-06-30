#example on how to create a tuple
#tuples are immutable

#how to create a tuple
tup=()

my_tuple = (100, "This is Cognitio", 52.36, 3.2j) #creating a tuple
print(my_tuple) # printing the variable data
print(type(my_tuple)) # printing the datatype
print(type(my_tuple[1]))
print(my_tuple[1])

###this will give an error
my_tuple[0] = 'I am happy'
