#example of creating list

#how to create a list, we create a list with []
a=[]
print(type(a))
print('This is an empty list: ', a)

new_list = [1, 2, 25, 53.56, 'ABC', 3.5j] #creating a list with various datatypes

print(new_list) #printing our variable
print(type(new_list))  #printing the datatype of the variable

#to check the mutability of the list
print(new_list[2])
print(type(new_list[2]))

#modify the element in the list
new_list[0] = 10000000000
print(new_list)

#using reverse indexing
print(new_list[-1])
print(new_list[5])
print(new_list[-2])

##################################
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alpha[0:])
print(alpha[0::5])
print(alpha[0::1])
print(alpha[0::2])
print(alpha[0:10])
print(alpha[0:10:2])
print(alpha[0::5])
print(alpha[10:])
print(alpha[10:15])
print(alpha[10:15:2])



