# If no exception is raised then else block is executed
## The following points for exception handling
## A single try block can be followed by several except block
## Multiple except blocks can be used to handle multiple exceptions
## We cannot write except blocks withouttry block
## We can write a try block without an except block
## Else block and finally blockd are not compulsary
## When there is no exception, else block is executed after try block
## Finally block is always executed

## an exception handlin example
##
## try:
##  print('This is try block'
##
## except
##
## else
##
## finally
##  print('This is a finally block')

#
try:
    f = open('myfile.txt', 'w')
    a,b = [int(x) for x in input('Enter two numbers: ').split()]
    a.append(b)
    c = a/b
    f.write(f'Writing{c} into myfile')

##except blocks are also called as handlers
except ZeroDivisionError:
    print('Division by zero happened')
    print('Please do not enter 0 in denominator')

except AttributeError:
    print('Attribute Not Supported.Attribute Error')

##
## except ValueError:
##   print('Please enter values separated by space.')
##
## except IOError:
##   print('Please enter correct mode')
##
## except KeyboardInterrupt:
##   print('User stopped the program')

### finally block always execute
finally:
    f.close()
    print('File is closed')
