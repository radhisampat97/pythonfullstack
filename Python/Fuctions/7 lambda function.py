##Anonymous Lambda function
#Lambda variable: expression

##x = 5
##y = 5
##z = x + y
##print(z)
##
##def sum(x,y):
##    z = x + y
##    print(z)
##
##sum (5,5)
##
##
### Lambda function to calculate sum of the values
##
##f = lambda x, y, z: (x+y)*z
##value = f(5,5,2)
##print()
##
##
#### lambda function to calculate multiplication of the values
##
##f = lambda x,y,z: x * y * z
##value = f(5,5,10)
##print('Multiplication of values is: ', value)
##print()
##
##
###### lambda function to find bigger number
####
####maxx = lambda x, y: x if x>y else y
####a, b = [int(n) for n in input('Enter two numbers: ').split()]
####print('Bigger number is: ', maxx(a,b))
####print()
##
##
####
###using lambdas with filter() function
###   filter(function, sequence)
##
### using filter() function filter put the even numbers from a list
##
##def is_even(x):
##    '''Doc string student should write'''
##    if x % 2 == 0:
##        return True
##    else:
##        return False
##
### let us take a list of numbers
##
##lst = [10,20,30,40,50,77,625,368814,5287,3451,54126]
####
### call the filter() with is_even and lst
##
##lst1 = list(filter(is_even, lst))
##print(lst1)
##
##lat1 = list(filter(lambda x:True if x % 2 == 0 else False, lst))
##print(lat1)
##print()
##
####
####map() function
###       map(function, sequence)
##
### map() function that gives square
##
def square(x):
    '''Doc string strudent should write'''
    return x*x

##### let us take a list of numbers
lst = [164,3145,614,611,4,10]

## to call map() function with squares() and lst

lst = list(map(square, lst))
print(lst)

lst1 = list(map(lambda x:x*x, lst))
print(lst1)
print()
####
####
####reduce() function
###       reduce(function, sequence)
##
##from functools import *
##lst = [1,2,3,4,5,6]
##
##result = reduce(lambda x,y: x*y, lst)
##print(result)
