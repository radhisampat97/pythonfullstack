## formal and actual areguments
#
## This Actual Arguments used in a function call are of 4 types
## 1 Positional arguments
## 2 Keyword arguments
## 3 Defaul arguments
## 4 Variable length arguments
##
# 1 Positional Arguments

def attach(s1,s2):
    '''to join s2 and s2 and display total string'''
    s3 = s1 + s2
    print(s3)

# call attach() and pass 2 strings

attach('New  ', 'York')
attach('York ', 'New')
print()
##
##
##
##
# 2 Keyword Argument

def grocery(product, price):
    '''This to display the given arguments'''
    print('Product: ', product)
    print('Price: ', price)

## call grocery() fucntion and pass 2 arguments
## grocery(100,Sugar)

grocery(price=100, product='Sugar')
print()

##
##
##
# Default arguments

def grocery(product, price=40.00):
    '''This to display the given arguments'''
    print('Product: ', product)
    print('Price: ', price)

# call the grocery() function and pass arguments

grocery(price=45.0, product='Sugar')
grocery(product='Sugar')
print()

##
##
##
# Variable arguments

def add(abc, *args):
    '''to add given number'''
    print('Formal Argument: ', abc)

    sum = 0
    for i in args:
        sum += i
    print('Sum of all numbers: ', (abc+sum))

# calling add() function and pass arguments
##add(5, 10)

add(50, 10,20,30,40,50)
print()
##s
## Variable length argument using a dictionary
##

def display(farg, **kwargs):
    """to display given values"""
    print('Formal Argument: ', farg)

    for x,y in kwargs.items():
        print(f'key = {x},  Value = {y}')

# calling the function
## display(5, rno=10)

print()

display(5, rno = 1, name = 'Radhika')
