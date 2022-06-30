## decorators in function

##def decor(fun):         # giftwrapping
##
##    def inner():
##        value = fun()       #access value returned by fun()
##        return value + 2    #increase the value by 2
##    return inner            #return the innder function
##
##
##@decor                  # calling the decorator function
##def num():
#### print(10)
##    return 10
##
##print(num())
##print()
##
##print(result_fun()) # call result_fun and display the result
##
##
##
##
# calling decorator function using '@' method

def decor_two(fun):

    def inner(*args,**kwargs):
        value = fun(*args,**kwargs)       #access value returned by fun()
        return value + 2    #increase the value by 2
    return inner            #return the innder function

# calling decorator function using '@' method

def decor_eight(fun):

    def inner(*args,**kwargs):
        value = fun(*args,**kwargs)       #access value returned by fun()
        return value + 8    #increase the value by 8
    return inner            #return the innder function

# take a function to which decorator should be applied
@decor_two
@decor_eight
def num(a,b):
    '''some statements process'''
    return a+b

#call decorator function and pass num
print(num(5,5))  # call result_fun and diplay the result
