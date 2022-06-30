# Functions are first class objects

# It is possible to assign a function to a variable
# It is possible to define one function inside another function
# It is possible to pass a function as parameter to anothe function
# It is possible that a function can return another function

# assign a function to a variable

def display(str):
    return 'Hi!' + str

# calling a function and assigning it function to variable x
x = display('Student')
print(x)


# define one function inside another function
def display(str):

    def message():
        return 'How are you'

    result = message() + str + '?'
    return result


# calling the function
print(display('Anurag'))
print(15*'--')


##
# fuctions can be passed as parameters to ther functions

def addition(fun):
    c = 10 + fun
    return c
##    return 'Hi' + fun

def number():
    return 100
##    return'How are you?'


## calling display() function and pass message() function
print(addition(number()))
print()
print(15*'----')

##
# function can return another function

def addition():

    def multiplication():
        print('This is multiplication')
        return 10*20

    def movie():
        print('This is a movie name')
        return 'Superman'

    return multiplication, movie

a, b = addition()
print(a())
print()

print(b())
print()

