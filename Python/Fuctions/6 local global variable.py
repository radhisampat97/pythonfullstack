## local variable in a function

##def myfunction():
##    a = 1     # this is a local variable
##    a += 1     # increment is
##    print("This is 'a' inside the function: ", a)  # display 2
##
### calling myfunction()
##myfunction()
##print(a)    #available

##======================================================

# global variable in a function

##a = 1         # this is a global variable
##def myfunction():
##    b = 2      # this is local variable
##    print('Printing value of "a" from within the function= ', a)  # display global variable
##    print('b inside the function= ', b)
##
##myfunction()
##
##print('Outside function a: ',a)  # available
##print(b)  #error , not available
##
#####
##==========================================================

# same name for global and local variable

##a = 11   # this is global variable
##def myfunction():
##    a=2   # this is local variable
##    print('inside function: ',a)  # display local variable
##
##myfunction()
##print('outside function: ',a)   # display global variable
##
##=============================================
##
# the GLOBAL Keyword
#program to access the global variable inside the function
## to modify it

##a = 10      # this is global varibale
##
####z = 100
#### print('This is first z: ',z)
##
##print('This is first a: ', a)
##
##def myfunction():
##    global a     # this is global variable
##    print('global a: ', a)
#### z=10
#### print('modified z = ', z) # display new value
##
##    a = 2  # modify global variable value
##    print('modified a: ', a)      #display modified value
##
#### calling function
##myfunction()
#### b = a + 1
#### print('Value of b: ',b)  
#### print('global z: ', z)  # display modified value
##
##print('global a: ', a)    # display modified value

##============================================
##
# same name for global and local varilable

a = 10         #this is global variable
def myfunction():
    a = 2    #a is a local variable
    x = globals()['a']  #get the global variable into x
    print('global variable a as x: ', x)
    print('local variable a: ', a)

myfunction()
print('global variable a: ', a)

