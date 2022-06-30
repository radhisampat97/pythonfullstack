## Returning Multiply Values from a function

def sum_sub(a,b):
    '''doc string'''
    c = a + b
    d = a - b
    z = a * b
    return c,d,z

# calling a function

p,q,r = sum_sub(10,20)
print(p,q,r, sep=',')

## defining variables
a = 50
b = 100

##p,q,r = sub_sum(a,b)
##print(p,q,r, sep=',')

## this will give the tuple with w elements

x = sum_sub(a,b)
print(x)
